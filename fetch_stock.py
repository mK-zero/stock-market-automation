import yfinance as yf # Update to polygon io api
from polygon import RESTClient
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv


# == API ==
load_dotenv()
API_KEY = os.getenv('POLYGON_API_KEY')

# == CONFIG ==

DAYS_BACK = 30
client = RESTClient(api_key=API_KEY)
ticker = "AAPL"

# == FETCH DATA ==
#data = yf.download(TICKER, period=DAYS, interval="1d")
# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2025-03-01", to="2025-07-31", limit=50000):
    aggs.append(a)

print(aggs)

# == CLEAN & SAVE ==
#filename = f"{ticker} _data_{datetime.now().date()}.csv"
#data.to_csv(filename)
#print(f"[X] Saved stock data to {filename}")

# == VISUALIZE ==
#plt.figure(figsize=(10, 4))
#plt.plot(data['Close'], label='Closing Price')
#plt.title(f"{TICKER} Closing Prices - Last{DAYS}")
#plt.xlabel("Date")
#plt.ylabel("Price ($)")
#plt.legend()
#plt.grid(True)
#plt.tight_layout()
#plt.savefig("stock_chart.png")
#print("[X] Saved stock chart as stock_chart.png")