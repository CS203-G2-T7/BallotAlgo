from FileIO.File_read_excel import read_excel_data_to_dataframe
import pgeocode
import pandas as pd

# nomi = pgeocode.Nominatim('sg')
# df = nomi.query_postal_code("822679")
# print(df)

# Check dataframe has only two columns, username and postal code.
# From dataframe, call pgeocode api to get lat and long from postal code.
# Add the lat and long columns to the dataframe. Return dataframe containing 4 columns (username: str, postal_code: str, lat: double, long: double)


def postal_to_lat_long(user_postal_code: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame()
