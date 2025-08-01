import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# == CONFIG ==
TICKER = "APPL"
DAYS = "30d"

# == FETCH DATA ==
data = yf.download(TICKER, period=DAYS, interval="1d")

# == CLEAN & SAVE ==
filename = f"{TICKER} _data_{datetime.now().date()}.csv"
data.to_csv(filename)
print(f"[X] Saved stock data to {filename}")

# == VISUALIZE ==
plt.figure(figsize=(10, 4))
plt.plot(data['Close'], label='Closing Price')
plt.title(f"{TICKER} Closing Prices - Last{DAYS}")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("stock_chart.png")
print("[X] Saved stock chart as stock_chart.png")