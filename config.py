import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "")
API_SECRET = os.getenv("API_SECRET", "")
USE_REAL_EXCHANGE = os.getenv("USE_REAL_EXCHANGE", "false").lower() == "true"
EXCHANGE_NAME = os.getenv("EXCHANGE_NAME", "binance")
SYMBOL = os.getenv("SYMBOL", "DOGE/USDT")
TIMEFRAME = os.getenv("TIMEFRAME", "1h")
LIMIT = int(os.getenv("LIMIT", "100"))
INITIAL_CASH = float(os.getenv("INITIAL_CASH", "10000"))
RISK_PER_TRADE = float(os.getenv("RISK_PER_TRADE", "0.02"))
MAX_POSITION_FRACTION = float(os.getenv("MAX_POSITION_FRACTION", "0.25"))
STOP_LOSS_PCT = float(os.getenv("STOP_LOSS_PCT", "0.05"))
TAKE_PROFIT_PCT = float(os.getenv("TAKE_PROFIT_PCT", "0.08"))
