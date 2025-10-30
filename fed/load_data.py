import os
import pandas_datareader.wb as wb
import pandas as pd

def load_gdp_data(countries, start=2000, end=2022):
    """Fetch GDP (current US$) data from the World Bank API and save locally."""
    save_path = 'data/gdp_data.csv'
    if os.path.exists(save_path):
        print("Using cached GDP data.")
        return pd.read_csv(save_path)
    
    df = wb.download(
        indicator='NY.GDP.MKTP.CD',
        country=countries,
        start=start,
        end=end
    ).rename(columns={'NY.GDP.MKTP.CD': 'gdp'}).reset_index()

    # create the directory if missing
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)

    print(f"Saved GDP data to {save_path}")
    return df