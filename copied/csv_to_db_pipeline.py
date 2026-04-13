"""
csv_to_db_pipeline.py

Reads and cleans data from a CSV file, then writes it to a database table
using SQLAlchemy. Ideal for data ingestion pipelines.
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging

# Setup
load_dotenv()
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Config
CSV_PATH = "data/users.csv"
DB_URL = os.getenv("DATABASE_URL")  # Example: 'sqlite:///users.db'

def clean_data(df):
    """Clean and normalize the DataFrame."""
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    df.dropna(subset=["email"], inplace=True)
    df['email'] = df['email'].str.strip().str.lower()
    return df

def write_to_db(df, table_name="users"):
    """Write DataFrame to a database table."""
    try:
        engine = create_engine(DB_URL)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Inserted {len(df)} records into '{table_name}' table.")
    except Exception as e:
        logging.error(f"Database write failed: {e}")

def main():
    try:
        df = pd.read_csv(CSV_PATH)
        logging.info(f"Loaded CSV with {len(df)} records.")
        cleaned = clean_data(df)
        write_to_db(cleaned)
    except FileNotFoundError:
        logging.error(f"File not found: {CSV_PATH}")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()

