import os
import pandas as pd
from dotenv import load_dotenv
from entsoe import EntsoePandasClient

load_dotenv()
API_KEY = os.getenv("ENTSOE_TOKEN")

client = EntsoePandasClient(api_key=API_KEY)

zone = "NO_1"
start = pd.Timestamp("20260101", tz="Europe/Oslo")
end = pd.Timestamp("20260401", tz="Europe/Oslo")

prices = client.query_day_ahead_prices(zone, start=start, end=end)
print("Raw prices pulled:", len(prices), "rows (15-min resolution)")

hourly = prices.resample("h").mean()
print("After resampling to hourly:", len(hourly), "rows")

df = hourly.reset_index()
df.columns = ["time", "price_eur_mwh"]

df.to_csv("../data/no1_prices.csv", index=False)

print("Saved to data/no1_prices.csv")
print(df.head())