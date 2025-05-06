from fastapi import FastAPI
import pandas as pd
app = FastAPI()
df = pd.read_csv("data.csv", encoding="latin-1").head(200)  # Limit to 200 rows for speed
@app.get("/data")
async def get_data():
    return df.to_dict(orient="records")