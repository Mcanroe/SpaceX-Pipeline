import polars as pl
import requests

url = "https://api.spacexdata.com/v5/launches"
response = requests.get(url)
data = response.json()

df = pl.DataFrame(data, infer_schema_length=1000)

print(df.head())
print(df.columns)
print(df.dtypes)
