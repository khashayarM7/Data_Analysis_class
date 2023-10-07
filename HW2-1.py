import matplotlib.pyplot as plt
import yfinance as yf

BTC = yf.download(tickers="BTC-USD", start="2020-09-01", end="2023-09-30", interval="1d")

# print(BTC)
# BTC["Benefit"] = BTC["Close"] - BTC["Open"]

plt.figure()

up = BTC[BTC.Close >= BTC.Open]

down = BTC[BTC.Open >= BTC.Close]

plt.bar(up.index, up.Close-up.Open, width=0.9, bottom=up.Open, color='green')
plt.bar(up.index, up.High-up.Close, width=0.2, bottom=up.Close, color='green')
plt.bar(up.index, up.Low-up.Open, width=0.2, bottom=up.Open, color='green')

plt.plot(up.index, up.High, marker='o', markersize=1.5, color='green', linestyle='-', linewidth=1)

plt.bar(down.index, down.Close-down.Open, width=0.9, bottom=down.Open, color='red')
plt.bar(down.index, down.High-down.Open, width=0.2, bottom=down.Open, color='red')
plt.bar(down.index, down.Low-down.Close, width=0.2, bottom=down.Close, color='red')

plt.plot(down.index, down.Low, marker='o', markersize=1.5, color='red', linestyle='-', linewidth=1)

plt.xticks(rotation=45)

plt.show()
