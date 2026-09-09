from app.indicators import Candle, assess_structure, sma


def test_sma_basic():
    assert sma([1, 2, 3, 4], 3) == [None, None, 2.0, 3.0]


def test_assess_structure_runs():
    candles = []
    price = 100.0
    for i in range(80):
        price += 0.1
        candles.append(Candle(start_ms=i * 60000, open=price - 0.05, high=price + 0.2, low=price - 0.2, close=price, volume=10 + i * 0.1))
    result = assess_structure(candles)
    assert "setup" in result
    assert "sma" in result
    assert "dmi_adx" in result
    assert "operational_view" in result
    assert "sma3_slope_1_pct" in result["sma"]
    assert "sma9_slope_2_pct" in result["sma"]
    assert "sma20_slope_5_pct" in result["sma"]
    assert "plus_di_slope_1" in result["dmi_adx"]
    assert "minus_di_slope_1" in result["dmi_adx"]
    assert "di_spread" in result["dmi_adx"]
    assert "ratio_to_ma20_pct" in result["volume"]
    assert result["operational_view"]["sma20"]["sticker"] is not None
