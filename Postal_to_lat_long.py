# from FileIO.File_read_excel import read_excel_data_to_dataframe
import pgeocode
import pandas as pd


# Check dataframe has only two columns, username and postal code.
# From dataframe, call pgeocode api to get lat and long from postal code.
# Add the lat and long columns to the dataframe. Return dataframe containing 4 columns (username: str, postal_code: str, lat: double, long: double)


def postal_to_lat_long(user_postal_code_df: pd.DataFrame) -> pd.DataFrame:
    for index, row in user_postal_code_df.iterrows():
        user_postal_code_df['Latitude'], user_postal_code_df['Longitude'] = get_lat_long(
            row.get('Postal Code'))
    return user_postal_code_df


def get_lat_long(postal_code: str) -> tuple:
    nomi = pgeocode.Nominatim('sg')
    df = nomi.query_postal_code(postal_code)
    return (df.get('latitude'), df.get('longitude'))


print(get_lat_long('679521'))
