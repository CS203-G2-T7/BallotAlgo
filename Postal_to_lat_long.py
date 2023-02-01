import math
import pgeocode
import pandas as pd


# Check dataframe has only two columns, username and postal code.
# From dataframe, call pgeocode api to get lat and long from postal code.
# Add the lat and long columns to the dataframe. Return dataframe containing 4 columns (username: str, postal_code: str, lat: double, long: double)

nomi = pgeocode.Nominatim('sg')


def postal_to_lat_long(df: pd.DataFrame) -> pd.DataFrame:
    lat_col, long_col = [], []
    print("Getting latitude and longitude...")

    for index, row in df.iterrows():
        lat, long = get_lat_long(row.get('Postal Code'))
        lat_col.append(lat)
        long_col.append(long)

    df = df.assign(
        Latitude=pd.Series(lat_col, dtype=pd.StringDtype()).values)
    df = df.assign(
        Longitude=pd.Series(long_col, dtype=pd.StringDtype()).values)
    # print(df)
    return df


def get_lat_long(postal_code: int) -> tuple:
    pc_length = int(math.log10(postal_code)) + 1
    valid_pc = (6 - pc_length) * "0" + \
        str(postal_code) if pc_length < 6 else str(postal_code)

    df = nomi.query_postal_code(valid_pc)
    lat, long = df.get('latitude'), df.get('longitude')
    if math.isnan(lat) or math.isnan(long):
        lat, long = ('1.3521', '103.8198')  # Defaults to centre of SG if NaN
    return (lat, long)


# print(get_lat_long('679521'))
