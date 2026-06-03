import pandas as pd

df = pd.read_csv("../data/practice_prices.csv")

print(df.head()) #first five

#in programming, exit code 0 means "finished successfully, no errors"

print(df["price_eur"]) #selecting a column, like SELECT, says type

average_price = df["price_eur"].mean()
highest_price = df["price_eur"].max()
lowest_price = df["price_eur"].min()

print("average price:", average_price)
print("highest price:", highest_price)
print("lowest price:", lowest_price)

import matplotlib.pyplot as plt

df.plot(x="hour", y="price_eur")
plt.show()

