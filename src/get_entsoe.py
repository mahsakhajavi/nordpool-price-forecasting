import os
import pandas as pd
from dotenv import load_dotenv
from entsoe import EntsoePandasClient

load_dotenv()
API_KEY = os.getenv("ENTSOE_TOKEN")

client = EntsoePandasClient(api_key=API_KEY)

#NO1, January 2026
zone = "NO_1"
start = pd.Timestamp("20260101", tz="Europe/Oslo")
end = pd.Timestamp("20260201", tz="Europe/Oslo")

prices = client.query_day_ahead_prices(zone, start=start, end=end)

print("Number of hourly prices:", len(prices))
print(prices.head())
print("average EUR/MWh:", prices.mean())