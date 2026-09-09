from __future__ import annotations

import os
from typing import Literal

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .indicators import Candle, assess_structure

BYBIT_BASE_URL = os.getenv("BYBIT_BASE_URL", "https://api.bybit.com")
ALLOWED_SYMBOLS = {s.strip().upper() for s in os.getenv("ALLOWED_SYMBOLS", "BTCUSDT,ETHUSDT,SOLUSDT,XRPUSDT,ADAUSDT").split(",") if s.strip()}

app = FastAPI(
    title="Wave Digital Coach Bridge",
    version="0.1.0",
    description=(
        "Read-only Bybit market-data bridge for a GPT trading coach. "
        "It fetches public candles and calculates SMA 3/9/20, DMI/ADX and Volume MA20. "
        "It does not trade, does not read balances, and does not require Bybit API keys."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


class CandleOut(BaseModel):
    start_ms: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    turnover: float | None = None


class MarketState(BaseModel):
    symbol: str
    category: str
    interval: str
    candles: list[CandleOut]
    analysis: dict = Field(default_factory=dict)


def _validate_symbol(symbol: str) -> str:
    symbol = symbol.upper().strip()
    if symbol not in ALLOWED_SYMBOLS:
        raise HTTPException(status_code=400, detail=f"Symbol not allowed. Allowed: {sorted(ALLOWED_SYMBOLS)}")
    return symbol


def _parse_bybit_candles(raw_list: list[list[str]]) -> list[Candle]:
    candles = [
        Candle(
            start_ms=int(row[0]),
            open=float(row[1]),
            high=float(row[2]),
            low=float(row[3]),
            close=float(row[4]),
            volume=float(row[5]),
            turnover=float(row[6]) if len(row) > 6 and row[6] not in (None, "") else None,
        )
        for row in raw_list
    ]
    return sorted(candles, key=lambda c: c.start_ms)


@app.get("/health", operation_id="health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "wave-digital-coach-bridge"}


@app.get("/market-state", response_model=MarketState, operation_id="getMarketState")
async def get_market_state(
    symbol: str = Query(default="BTCUSDT", description="Trading symbol, e.g. BTCUSDT."),
    interval: str = Query(default="1", description="Bybit candle interval. Use 1 for 1 minute."),
    category: Literal["linear", "spot", "inverse"] = Query(default="linear", description="Bybit product category."),
    limit: int = Query(default=200, ge=50, le=1000, description="Number of candles to fetch."),
) -> MarketState:
    symbol = _validate_symbol(symbol)
    params = {"category": category, "symbol": symbol, "interval": interval, "limit": limit}
    url = f"{BYBIT_BASE_URL}/v5/market/kline"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            payload = response.json()
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail=f"Bybit request failed: {exc}") from exc

    if payload.get("retCode") != 0:
        raise HTTPException(status_code=502, detail={"bybit_error": payload})

    raw_list = payload.get("result", {}).get("list", [])
    if len(raw_list) < 50:
        raise HTTPException(status_code=502, detail="Not enough candles returned by Bybit.")

    candles = _parse_bybit_candles(raw_list)
    analysis = assess_structure(candles)

    return MarketState(
        symbol=symbol,
        category=category,
        interval=interval,
        candles=[CandleOut(**c.__dict__) for c in candles[-120:]],
        analysis=analysis,
    )
