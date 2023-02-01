import pandas as pd
import os
from dotenv import load_dotenv
import asyncio

from FileIO.File_read_excel import read_excel_data_to_dataframe
from FileIO.File_write_excel import write_dataframe_to_excel
from Postal_to_lat_long import postal_to_lat_long

# TODO: Write main method calling all other functions.
load_dotenv()


raw_df = read_excel_data_to_dataframe("test.xlsx")
valid_df = raw_df

# Lat and long not found in df. Need to memoise.
if raw_df.get('Latitude') is None or raw_df.get('Longitude') is None:
    valid_df = postal_to_lat_long(raw_df)
    write_dataframe_to_excel(valid_df, "test.xlsx")
else:
    print("Latitude and longitude is already cached.")
