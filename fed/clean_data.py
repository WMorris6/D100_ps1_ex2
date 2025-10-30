import pandas as pd

def clean_gdp_data(df):
    """
    Clean and prepare GDP data:
    - Rename columns
    - Remove missing GDP values
    - Convert GDP to trillions for readability
    - Sort by country and year
    """
    df.columns = [c.lower().strip() for c in df.columns]
    df = df.dropna(subset=["gdp"])
    df["gdp_trillions"] = df["gdp"] / 1e12
    df = df.sort_values(["country", "year"])
    return df
