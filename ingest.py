import requests
import pandas as pd
response = requests.get("http://127.0.0.1:8000/data")
data = response.json()
df = pd.DataFrame(data)
df.to_csv("raw_data.csv", index=False)
print("Data ingested successfully!")