from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


@dataclass(frozen=True)
class Candle:
    start_ms: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    turnover: float | None = None


def sma(values: list[float], period: int) -> list[float | None]:
    if period <= 0:
        raise ValueError("period must be positive")
    out: list[float | None] = []
    rolling = 0.0
    for i, value in enumerate(values):
        rolling += value
        if i >= period:
            rolling -= values[i - period]
        if i + 1 >= period:
            out.append(rolling / period)
        else:
            out.append(None)
    return out


def wilder_smooth(values: list[float], period: int) -> list[float | None]:
    """Wilder smoothing used by DMI/ADX.

    Returns None until there are enough values to initialize the smoothed series.
    """
    if period <= 0:
        raise ValueError("period must be positive")
    out: list[float | None] = [None] * len(values)
    if len(values) < period:
        return out

    first = sum(values[:period])
    out[period - 1] = first
    prev = first
    for i in range(period, len(values)):
        prev = prev - (prev / period) + values[i]
        out[i] = prev
    return out


def dmi_adx(candles: list[Candle], period: int = 14, adx_smoothing: int = 14) -> dict[str, list[float | None]]:
    """Calculate +DI, -DI, DX, ADX using Wilder's method.

    Intended for signal support, not as a standalone trading trigger.
    """
    if period <= 1 or adx_smoothing <= 1:
        raise ValueError("period and adx_smoothing must be > 1")

    n = len(candles)
    plus_dm: list[float] = [0.0] * n
    minus_dm: list[float] = [0.0] * n
    tr: list[float] = [0.0] * n

    for i in range(1, n):
        current = candles[i]
        previous = candles[i - 1]
        up_move = current.high - previous.high
        down_move = previous.low - current.low
        plus_dm[i] = up_move if up_move > down_move and up_move > 0 else 0.0
        minus_dm[i] = down_move if down_move > up_move and down_move > 0 else 0.0
        tr[i] = max(
            current.high - current.low,
            abs(current.high - previous.close),
            abs(current.low - previous.close),
        )

    atr_s = wilder_smooth(tr[1:], period)
    plus_s = wilder_smooth(plus_dm[1:], period)
    minus_s = wilder_smooth(minus_dm[1:], period)

    # Re-pad to candle length because we smoothed from index 1 onward.
    atr = [None] + atr_s
    plus_smoothed = [None] + plus_s
    minus_smoothed = [None] + minus_s

    plus_di: list[float | None] = [None] * n
    minus_di: list[float | None] = [None] * n
    dx: list[float | None] = [None] * n

    for i in range(n):
        if atr[i] is None or plus_smoothed[i] is None or minus_smoothed[i] is None or atr[i] == 0:
            continue
        pdi = 100.0 * plus_smoothed[i] / atr[i]
        mdi = 100.0 * minus_smoothed[i] / atr[i]
        plus_di[i] = pdi
        minus_di[i] = mdi
        denom = pdi + mdi
        dx[i] = 100.0 * abs(pdi - mdi) / denom if denom else None

    dx_for_smoothing = [value if value is not None else 0.0 for value in dx]
    adx_raw = wilder_smooth(dx_for_smoothing, adx_smoothing)
    adx: list[float | None] = [None] * n
    for i, value in enumerate(adx_raw):
        if value is not None:
            adx[i] = value / adx_smoothing

    return {"plus_di": plus_di, "minus_di": minus_di, "dx": dx, "adx": adx}


def slope_pct(series: list[float | None], lookback: int = 3) -> float | None:
    if lookback <= 0 or len(series) <= lookback:
        return None
    latest = series[-1]
    previous = series[-1 - lookback]
    if latest is None or previous is None or previous == 0:
        return None
    return (latest - previous) / previous * 100.0


def slope_delta(series: list[float | None], lookback: int = 1) -> float | None:
    if lookback <= 0 or len(series) <= lookback:
        return None
    latest = series[-1]
    previous = series[-1 - lookback]
    if latest is None or previous is None:
        return None
    return latest - previous


def latest_non_null(series: Iterable[float | None]) -> float | None:
    for value in reversed(list(series)):
        if value is not None:
            return value
    return None


def _round(value: float | None, ndigits: int = 6) -> float | None:
    return round(value, ndigits) if value is not None else None


def _slope_sticker(value: float | None, flat_threshold: float) -> str:
    if value is None:
        return "⚪?"
    if value > flat_threshold:
        return "🟢↑"
    if value < -flat_threshold:
        return "🔴↓"
    return "🟡↔"


def _minus_di_sticker(value: float | None, flat_threshold: float = 0.5) -> str:
    if value is None:
        return "⚪?"
    if value > flat_threshold:
        return "🔴↑"
    if value < -flat_threshold:
        return "🔴↓"
    return "🟡↔"


def _plus_di_sticker(value: float | None, flat_threshold: float = 0.5) -> str:
    if value is None:
        return "⚪?"
    if value > flat_threshold:
        return "🟢↑"
    if value < -flat_threshold:
        return "🟢↓"
    return "🟡↔"


def _spread_sticker(change: float | None, plus_dominates: bool, minus_dominates: bool, flat_threshold: float = 0.5) -> str:
    if change is None:
        return "⚪?"
    if abs(change) <= flat_threshold:
        return "🟡↔"
    if change > 0 and minus_dominates:
        return "🔴↗"
    if change > 0 and plus_dominates:
        return "🟢↗"
    if change < 0:
        return "🟡↘"
    return "⚪?"


def _distance_label(distance_pct: float | None) -> str:
    if distance_pct is None:
        return "unknown"
    abs_distance = abs(distance_pct)
    if abs_distance <= 0.10:
        return "near"
    if abs_distance <= 0.25:
        return "normal"
    return "extended"


def _volume_quality(ratio_pct: float | None) -> str:
    if ratio_pct is None:
        return "unknown"
    if ratio_pct < 35:
        return "very_low"
    if ratio_pct < 50:
        return "low"
    if ratio_pct < 100:
        return "below_average"
    return "healthy_or_high"


def assess_structure(candles: list[Candle]) -> dict[str, Any]:
    closes = [c.close for c in candles]
    volumes = [c.volume for c in candles]
    sma3 = sma(closes, 3)
    sma9 = sma(closes, 9)
    sma20 = sma(closes, 20)
    vol_ma20 = sma(volumes, 20)
    dmi = dmi_adx(candles, 14, 14)

    last_close = closes[-1]
    last_sma3 = latest_non_null(sma3)
    last_sma9 = latest_non_null(sma9)
    last_sma20 = latest_non_null(sma20)
    last_plus_di = latest_non_null(dmi["plus_di"])
    last_minus_di = latest_non_null(dmi["minus_di"])
    last_adx = latest_non_null(dmi["adx"])
    last_vol = volumes[-1]
    last_vol_ma20 = latest_non_null(vol_ma20)

    sma3_slope_1 = slope_pct(sma3, 1)
    sma3_slope_2 = slope_pct(sma3, 2)
    sma3_slope_3 = slope_pct(sma3, 3)
    sma9_slope_2 = slope_pct(sma9, 2)
    sma9_slope_3 = slope_pct(sma9, 3)
    sma20_slope_3 = slope_pct(sma20, 3)
    sma20_slope_5 = slope_pct(sma20, 5)

    plus_di_slope_1 = slope_delta(dmi["plus_di"], 1)
    plus_di_slope_3 = slope_delta(dmi["plus_di"], 3)
    minus_di_slope_1 = slope_delta(dmi["minus_di"], 1)
    minus_di_slope_3 = slope_delta(dmi["minus_di"], 3)
    adx_slope_3 = slope_delta(dmi["adx"], 3)

    bullish_stack = bool(last_sma3 and last_sma9 and last_sma20 and last_sma3 > last_sma9 > last_sma20)
    bearish_stack = bool(last_sma3 and last_sma9 and last_sma20 and last_sma3 < last_sma9 < last_sma20)
    above_sma20 = bool(last_sma20 and last_close > last_sma20)
    below_sma20 = bool(last_sma20 and last_close < last_sma20)
    plus_dominates = bool(last_plus_di is not None and last_minus_di is not None and last_plus_di > last_minus_di)
    minus_dominates = bool(last_plus_di is not None and last_minus_di is not None and last_minus_di > last_plus_di)

    sma_gap_3_9_pct = None
    sma_gap_9_20_pct = None
    if last_sma3 and last_sma9 and last_close:
        sma_gap_3_9_pct = abs(last_sma3 - last_sma9) / last_close * 100.0
    if last_sma9 and last_sma20 and last_close:
        sma_gap_9_20_pct = abs(last_sma9 - last_sma20) / last_close * 100.0

    compressed = False
    if sma_gap_3_9_pct is not None and sma_gap_9_20_pct is not None:
        compressed = sma_gap_3_9_pct < 0.03 and sma_gap_9_20_pct < 0.05

    price_to_sma9_pct = None
    price_to_sma20_pct = None
    if last_sma9:
        price_to_sma9_pct = (last_close - last_sma9) / last_sma9 * 100.0
    if last_sma20:
        price_to_sma20_pct = (last_close - last_sma20) / last_sma20 * 100.0

    di_spread = None
    if last_plus_di is not None and last_minus_di is not None:
        di_spread = abs(last_plus_di - last_minus_di)

    plus_di_series = dmi["plus_di"]
    minus_di_series = dmi["minus_di"]
    di_spread_series: list[float | None] = [
        abs(p - m) if p is not None and m is not None else None
        for p, m in zip(plus_di_series, minus_di_series)
    ]
    di_spread_change_1 = slope_delta(di_spread_series, 1)
    di_spread_change_3 = slope_delta(di_spread_series, 3)

    volume_ratio_to_ma20 = None
    if last_vol_ma20 and last_vol_ma20 > 0:
        volume_ratio_to_ma20 = last_vol / last_vol_ma20 * 100.0

    long_score = 0
    short_score = 0
    reasons: list[str] = []

    if bullish_stack:
        long_score += 2
        reasons.append("SMA3>SMA9>SMA20")
    if bearish_stack:
        short_score += 2
        reasons.append("SMA3<SMA9<SMA20")
    if sma20_slope_3 is not None and sma20_slope_3 > 0:
        long_score += 1
    if sma20_slope_3 is not None and sma20_slope_3 < 0:
        short_score += 1
    if above_sma20:
        long_score += 1
    if below_sma20:
        short_score += 1
    if plus_dominates:
        long_score += 2
        reasons.append("+DI domina -DI")
    if minus_dominates:
        short_score += 2
        reasons.append("-DI domina +DI")
    if last_adx is not None and last_adx >= 18:
        if plus_dominates:
            long_score += 1
        if minus_dominates:
            short_score += 1
    if not compressed:
        long_score += 1
        short_score += 1
    else:
        reasons.append("SMA3/9/20 comprimidas: cuidado con lateralidad")

    if last_vol_ma20 and last_vol > last_vol_ma20:
        reasons.append("Volumen sobre media 20")

    if long_score >= 7 and long_score > short_score:
        setup = "LONG_CANDIDATE"
        action = "Vigilar compra solo con vela verde de confirmación y riesgo definido."
    elif short_score >= 7 and short_score > long_score:
        setup = "SHORT_CANDIDATE"
        action = "Vigilar venta/short solo con vela roja de confirmación y riesgo definido."
    elif compressed:
        setup = "NO_TRADE_COMPRESSION"
        action = "No operar: medias comprimidas o mercado lateral."
    else:
        setup = "WAIT"
        action = "Esperar confirmación; no hay ventaja limpia."

    if volume_ratio_to_ma20 is not None and volume_ratio_to_ma20 < 35 and setup in {"LONG_CANDIDATE", "SHORT_CANDIDATE"}:
        setup = "WAIT_WEAK_VOLUME"
        action = "Esperar: el volumen actual es extremadamente bajo frente a MA20."

    operational_view = {
        "price": {
            "value": round(last_close, 8),
            "to_sma9_pct": _round(price_to_sma9_pct, 6),
            "to_sma20_pct": _round(price_to_sma20_pct, 6),
            "zone_vs_sma9": _distance_label(price_to_sma9_pct),
            "zone_vs_sma20": _distance_label(price_to_sma20_pct),
        },
        "sma3": {
            "value": _round(last_sma3, 8),
            "slope_1_pct": _round(sma3_slope_1, 6),
            "slope_2_pct": _round(sma3_slope_2, 6),
            "sticker": _slope_sticker(sma3_slope_1, 0.005),
        },
        "sma9": {
            "value": _round(last_sma9, 8),
            "slope_2_pct": _round(sma9_slope_2, 6),
            "slope_3_pct": _round(sma9_slope_3, 6),
            "sticker": _slope_sticker(sma9_slope_2, 0.005),
        },
        "sma20": {
            "value": _round(last_sma20, 8),
            "slope_3_pct": _round(sma20_slope_3, 6),
            "slope_5_pct": _round(sma20_slope_5, 6),
            "sticker": _slope_sticker(sma20_slope_3, 0.005),
        },
        "plus_di": {
            "value": _round(last_plus_di, 4),
            "slope_1": _round(plus_di_slope_1, 4),
            "slope_3": _round(plus_di_slope_3, 4),
            "sticker": _plus_di_sticker(plus_di_slope_1),
        },
        "minus_di": {
            "value": _round(last_minus_di, 4),
            "slope_1": _round(minus_di_slope_1, 4),
            "slope_3": _round(minus_di_slope_3, 4),
            "sticker": _minus_di_sticker(minus_di_slope_1),
        },
        "di_spread": {
            "value": _round(di_spread, 4),
            "change_1": _round(di_spread_change_1, 4),
            "change_3": _round(di_spread_change_3, 4),
            "sticker": _spread_sticker(di_spread_change_1, plus_dominates, minus_dominates),
        },
        "adx": {
            "value": _round(last_adx, 4),
            "slope_3": _round(adx_slope_3, 4),
            "sticker": _slope_sticker(adx_slope_3, 0.5),
        },
        "volume": {
            "last": round(last_vol, 8),
            "ma20": _round(last_vol_ma20, 8),
            "ratio_to_ma20_pct": _round(volume_ratio_to_ma20, 2),
            "quality": _volume_quality(volume_ratio_to_ma20),
            "sticker": "⚠️" if volume_ratio_to_ma20 is not None and volume_ratio_to_ma20 < 50 else "🟢",
        },
    }

    return {
        "price": round(last_close, 8),
        "sma": {
            "sma3": _round(last_sma3, 8),
            "sma9": _round(last_sma9, 8),
            "sma20": _round(last_sma20, 8),
            "sma3_slope_1_pct": _round(sma3_slope_1, 6),
            "sma3_slope_2_pct": _round(sma3_slope_2, 6),
            "sma3_slope_3_pct": _round(sma3_slope_3, 6),
            "sma9_slope_2_pct": _round(sma9_slope_2, 6),
            "sma9_slope_3_pct": _round(sma9_slope_3, 6),
            "sma20_slope_3_pct": _round(sma20_slope_3, 6),
            "sma20_slope_5_pct": _round(sma20_slope_5, 6),
            "gap_3_9_pct": _round(sma_gap_3_9_pct, 6),
            "gap_9_20_pct": _round(sma_gap_9_20_pct, 6),
            "price_to_sma9_pct": _round(price_to_sma9_pct, 6),
            "price_to_sma20_pct": _round(price_to_sma20_pct, 6),
            "compressed": compressed,
        },
        "dmi_adx": {
            "plus_di": _round(last_plus_di, 4),
            "minus_di": _round(last_minus_di, 4),
            "adx": _round(last_adx, 4),
            "plus_di_slope_1": _round(plus_di_slope_1, 4),
            "plus_di_slope_3": _round(plus_di_slope_3, 4),
            "minus_di_slope_1": _round(minus_di_slope_1, 4),
            "minus_di_slope_3": _round(minus_di_slope_3, 4),
            "adx_slope_3": _round(adx_slope_3, 4),
            "di_spread": _round(di_spread, 4),
            "di_spread_change_1": _round(di_spread_change_1, 4),
            "di_spread_change_3": _round(di_spread_change_3, 4),
        },
        "volume": {
            "last": round(last_vol, 8),
            "ma20": _round(last_vol_ma20, 8),
            "ratio_to_ma20_pct": _round(volume_ratio_to_ma20, 2),
            "quality": _volume_quality(volume_ratio_to_ma20),
            "above_ma20": bool(last_vol_ma20 and last_vol > last_vol_ma20),
        },
        "operational_view": operational_view,
        "scores": {"long": long_score, "short": short_score},
        "setup": setup,
        "action": action,
        "reasons": reasons,
    }
