import pandas as pd
import os
from dotenv import load_dotenv

from FileIO.File_read_excel import read_excel_data_to_dataframe

# TODO: Write main method calling all other functions.
load_dotenv()

raw_df = read_excel_data_to_dataframe(os.getenv("FILENAME"))

if raw_df.get('Latitude') is None or raw_df.get('Longitude') is None:
    print("Should run postal to lat long")
