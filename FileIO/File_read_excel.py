import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def read_excel_data_to_dataframe(filename: str) -> pd.DataFrame:
    try:
        return pd.read_csv('/content/gdrive/MyDrive/Colab Notebooks/BallotAlgo/Excel/' + filename)
    except FileNotFoundError as e:
        print(f"File not found\n{e}")
    except Exception as e:
        print(f"Unknown exception\n{e}")
    return pd.DataFrame({})


# df = read_excel_data_to_dataframe()
# print(postal_to_lat_long(df))
