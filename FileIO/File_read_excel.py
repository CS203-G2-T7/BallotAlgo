import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Reads xlsx file and returns a dataframe. May or may not have lat long columns.


def read_excel_data_to_dataframe(filename: str = 'Excel/' + os.getenv("FILENAME")) -> pd.DataFrame:
    try:
        return pd.read_excel('Excel/' + filename)
    except FileNotFoundError as e:
        print("File not found")
        print(e)
    except Exception as e:
        print("Unknown exception")
        print(e)
    return pd.DataFrame({})


# print(read_excel_data_to_dataframe())
# print(read_excel_data_to_dataframe())  # None


def postal_to_lat_long(user_postal_code_df: pd.DataFrame) -> pd.DataFrame:
    for index, row in user_postal_code_df.iterrows():
        user_postal_code_df['Latitude'] = index + 1
        user_postal_code_df['Longitude'] = index - 1
    return user_postal_code_df


# df = read_excel_data_to_dataframe()
# print(postal_to_lat_long(df))
