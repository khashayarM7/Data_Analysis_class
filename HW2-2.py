import pandas as pd
import numpy as np

BTC = pd.read_csv("/Users/khashayar/Desktop/Data Analysis/DA 02/BTC-USD.csv")

BTC["New_Close"] = BTC["Close"].shift(-1)

print(BTC.Close, BTC.New_Close)

my_array = BTC["Close"]

result_array = np.lib.stride_tricks.sliding_window_view(my_array, (3,))

result_list = result_array.tolist()

BTC = BTC[:-2]

BTC["New_Close3"] = result_list

print(BTC.New_Close3)
