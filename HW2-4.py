import matplotlib.pyplot as plt
import yfinance as yf

# download from yahoo finance BTC-USD with specific date and interval.
BTC = yf.download(tickers="BTC-USD", start="2020-01-01", end="2023-09-30", interval="1d")

# make subplot with 2 plot in 1 fig next to each other.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# make range for up and down to specific them
up = BTC[BTC.Close >= BTC.Open]
down = BTC[BTC.Open >= BTC.Close]

# plot 'up' candles section with green color.
ax1.bar(up.index, up.Close - up.Open, width=0.9, bottom=up.Open, color="green")
ax1.bar(up.index, up.High - up.Close, width=0.2, bottom=up.Close, color="green")
ax1.bar(up.index, up.Low - up.Open, width=0.2, bottom=up.Open, color="green")

# connect high up candles together with green line.
# ax1.plot(up.index, up.High, color="green", linestyle='-', linewidth=1)

# make 'o' marker in head of 'up' high candles.
# ax1.plot(up.index, up.High, marker="o", markersize=1.5, color="green", linestyle='-', linewidth=1)

ax1.set_xticks(up.index)
ax1.set_xticklabels(up.index, rotation=45)
ax1.set_title("Green Candles")

# plot down candles together with red line.
ax2.bar(down.index, down.Close - down.Open, width=0.9, bottom=down.Open, color='red')
ax2.bar(down.index, down.High - down.Open, width=0.2, bottom=down.Open, color='red')
ax2.bar(down.index, down.Low - down.Close, width=0.2, bottom=down.Close, color='red')

# connect low down candles together with red line.
# ax2.plot(down.index, down.Low, color='red', linestyle='-', linewidth=1)

# make 'o' marker in head of 'low' down candles.
#ax2.plot(down.index, down.Low, marker='o', markersize=1.5, color='red', linestyle='-', linewidth=1)

ax2.set_xticks(down.index)
ax2.set_xticklabels(down.index, rotation=45)
ax2.set_title("Red Candles")

plt.tight_layout()
plt.show()
