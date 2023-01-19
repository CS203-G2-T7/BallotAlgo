import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Reads xlsx file and returns a dataframe. May or may not have lat long columns.


def read_excel_data_to_dataframe(filename: str = os.getenv("FILENAME")) -> pd.DataFrame:
    try:
        print(filename)
        return pd.read_excel(filename)
    except FileNotFoundError:
        print("File not found")
        print(FileNotFoundError.with_traceback())
    except Exception as e:
        print("Unknown exception")
        print(e.with_traceback())
    return pd.DataFrame({})


# print(read_excel_data_to_dataframe())
