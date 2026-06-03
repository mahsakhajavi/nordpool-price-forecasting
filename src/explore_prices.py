import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/no1_prices.csv")

df["time"] = pd.to_datetime(df["time"], utc=True)

print(df.head())
print("rows:", len(df))
print("average price:", df["price_eur_mwh"].mean())
print("highest price:", df["price_eur_mwh"].max())
print("lowest price:", df["price_eur_mwh"].min())

df.plot(x="time", y="price_eur_mwh", figsize=(12, 5))
plt.title("NO1 (Oslo) hourly day-ahead price, Jan–Mar 2026")
plt.ylabel("EUR per MWh")
plt.show()