import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Check df has lat long columns.
# Overwrite excel file with the dataframe. Username, postal code should have no change.
# Only the lat and long columns added.


def write_dataframe_to_excel(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, index=False)
    return
