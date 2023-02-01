import pandas as pd
import os
from dotenv import load_dotenv

from FileIO.File_read_excel import read_excel_data_to_dataframe
from FileIO.File_write_excel import write_dataframe_to_excel
from Postal_to_lat_long import postal_to_lat_long
from Lat_long_to_distance import lat_long_to_distance
from Ballot_selector import ballot_selector

# TODO: Write main method calling all other functions.
load_dotenv()


garden_c_df = read_excel_data_to_dataframe("Garden_coordinates.xlsx")
garden_c = garden_c_df.loc[garden_c_df['Garden'] == os.getenv("GARDEN")]
garden_lat, garden_long = garden_c.iloc[0]['Latitude'], garden_c.iloc[0]['Longitude']
# print(garden_c)

raw_df = read_excel_data_to_dataframe("test.xlsx")
valid_df = raw_df

# Lat and long not found in df. Need to memoise.
if raw_df.get('Latitude') is None or raw_df.get('Longitude') is None:
    valid_df = postal_to_lat_long(raw_df)
    write_dataframe_to_excel(valid_df, "test.xlsx")
else:
    print("Latitude and longitude already cached.")

user_dist: dict = {}
dist_weights = {1: 10, 2: 5, 5: 1}

for index, row in valid_df.iterrows():
    user_dist[row.get('S/N')] = lat_long_to_distance(garden_lat,
                                                     garden_long, row.get('Latitude'), row.get('Longitude'))

winners = ballot_selector(user_dist, 5, dist_weights)
for w in winners:
    print(f'{w} | {user_dist[w]}')
