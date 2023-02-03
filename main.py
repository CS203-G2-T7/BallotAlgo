import pandas as pd
import os
import ast
from dotenv import load_dotenv

from FileIO.File_read_excel import read_excel_data_to_dataframe
from FileIO.File_write_excel import write_dataframe_to_excel
from Postal_to_lat_long import postal_to_lat_long
from Lat_long_to_distance import lat_long_to_distance
from Ballot_selector import ballot_selector

load_dotenv()
FILENAME = os.getenv("FILENAME")
GARDEN = os.getenv("GARDEN")
NUM_PLOTS = os.getenv("NUM_PLOTS")
DIST_WEIGHTS = ast.literal_eval(os.getenv("DIST_WEIGHTS"))
CEILING = float(os.getenv("CEILING"))

garden_c_df = read_excel_data_to_dataframe("Garden_coordinates.xlsx")
garden_c = garden_c_df.loc[garden_c_df['Garden'] == GARDEN]
garden_lat, garden_long = garden_c.iloc[0]['Latitude'], garden_c.iloc[0]['Longitude']

raw_df = read_excel_data_to_dataframe(FILENAME)
valid_df = raw_df

if raw_df.get('Latitude') is None or raw_df.get('Longitude') is None:
    valid_df = postal_to_lat_long(raw_df)
else:
    print("Latitude and longitude already cached.")

user_dist: dict = {}

for index, row in valid_df.iterrows():
    user_dist[row.get('S/N')] = lat_long_to_distance(garden_lat,
                                                     garden_long, float(row.get('Latitude')), float(row.get('Longitude')))
# Add dist column to excel
dist_col = list(user_dist.values())
valid_df = valid_df.assign(
    Distance=pd.Series(dist_col, dtype=pd.StringDtype()).values)
write_dataframe_to_excel(valid_df, FILENAME)

winners: list = ballot_selector(
    user_dist, int(NUM_PLOTS), DIST_WEIGHTS, CEILING)

# Create df and write to excel
winner_df = pd.DataFrame(
    columns=['S/N', 'Postal Code', 'Latitude', 'Longitude', 'Distance'])

for i, w in enumerate(winners):
    w_valid_row = valid_df.loc[valid_df['S/N'] == w]
    p_code, lat, long = w_valid_row.iloc[0]['Postal Code'], w_valid_row.iloc[
        0]['Latitude'], w_valid_row.iloc[0]['Longitude']
    winner_df.loc[i] = [w] + [p_code] + [lat] + [long] + [user_dist[w]]

write_dataframe_to_excel(winner_df, FILENAME, "winner")

print(winner_df)
