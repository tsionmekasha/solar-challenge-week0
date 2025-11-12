import pandas as pd
import os

# Make sure paths are relative to project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_data(country_name):
    """
    Load cleaned dataset for a single country and add a 'Country' column.
    """
    country_files = {
        "benin": os.path.join(BASE_DIR, "data/cleaned/benin-malanville_clean.csv"),
        "sierra leone": os.path.join(BASE_DIR, "data/cleaned/sierraleone-bumbuna_clean.csv"),
        "togo": os.path.join(BASE_DIR, "data/cleaned/togo_clean.csv")
    }

    path = country_files.get(country_name.lower())
    if path is None or not os.path.exists(path):
        raise FileNotFoundError(f"No cleaned CSV found for country: {country_name}")

    df = pd.read_csv(path, parse_dates=['Timestamp'])

    # Add Country column
    df['Country'] = country_name.title()

    # Ensure 'Comments' exists
    if 'Comments' not in df.columns:
        df['Comments'] = ""

    return df

def load_all_countries():
    """
    Load and combine all cleaned country datasets.
    """
    dfs = []
    for country in ["benin", "sierra leone", "togo"]:
        df = load_data(country)
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df
