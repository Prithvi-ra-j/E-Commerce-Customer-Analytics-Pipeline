from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:Pass%40123@localhost:5432/ecommerce")
with engine.connect() as connection:
    print("Connection successful!")