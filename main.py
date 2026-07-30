import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict

from config import INITIAL_CASH, SYMBOL, TIMEFRAME
from data.feed import get_ohlcv
from execution.paper import PaperBroker
from risk.rules import RiskManager
from strategy.signal import build_signal


def append_log(entry: Dict[str, object]) -> None:
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    log_path = logs_dir / "paper_bot.log"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry) + "\n")


def run_bot(cycles: int, symbol: str = SYMBOL, timeframe: str = TIMEFRAME) -> None:
    broker = PaperBroker(initial_cash=INITIAL_CASH)
    risk_manager = RiskManager()

    print(f"Starting paper bot for {symbol} on {timeframe}")
    print(f"Initial cash: ${broker.cash:,.2f}")

    for index in range(1, cycles + 1):
        candles = get_ohlcv(symbol=symbol, timeframe=timeframe, limit=100)
        signal_data = build_signal(candles)
        current_price = candles[-1][4]
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        signal = signal_data["signal"]
        if broker.position_units > 0 and risk_manager.should_exit(broker.entry_price, current_price):
            signal = "sell"
            reason = "risk-exit"
        elif broker.position_units > 0:
            signal = "hold"
            reason = "position-open"
        else:
            reason = "signal"

        if signal == "buy":
            units = risk_manager.position_size_for_buy(broker.cash, current_price)
            trade = broker.buy(price=current_price, units=units, timestamp=timestamp, reason=reason)
            if trade:
                print(f"[{index}/{cycles}] BUY  @ {current_price:.4f} | units={trade['units']} | cash=${broker.cash:,.2f}")
        elif signal == "sell":
            trade = broker.sell(price=current_price, timestamp=timestamp, reason=reason)
            if trade:
                print(f"[{index}/{cycles}] SELL @ {current_price:.4f} | cash=${broker.cash:,.2f}")
        else:
            print(f"[{index}/{cycles}] HOLD @ {current_price:.4f} | signal={signal_data['signal']} | rsi={signal_data['rsi']}")

        state = {
            "timestamp": timestamp,
            "cycle": index,
            "symbol": symbol,
            "price": round(current_price, 6),
            "signal": signal,
            "rsi": signal_data["rsi"],
            "volume_ratio": signal_data["volume_ratio"],
            "cash": round(broker.cash, 6),
            "position_units": round(broker.position_units, 6),
            "entry_price": round(broker.entry_price, 6),
            "portfolio_value": round(broker.current_value(current_price), 2),
        }
        append_log(state)

    final_value = broker.current_value(candles[-1][4]) if candles else broker.current_value(0)
    print("Final portfolio value:", f"${final_value:,.2f}")
    summary = broker.summary()
    print("Final state:", summary)
    return {
        "final_portfolio_value": round(final_value, 2),
        "summary": summary,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a starter paper-trading memecoin bot")
    parser.add_argument("--cycles", type=int, default=8, help="How many bot iterations to simulate")
    parser.add_argument("--symbol", type=str, default=SYMBOL, help="Trading symbol")
    parser.add_argument("--timeframe", type=str, default=TIMEFRAME, help="Candle timeframe")
    args = parser.parse_args()
    run_bot(args.cycles, symbol=args.symbol, timeframe=args.timeframe)
