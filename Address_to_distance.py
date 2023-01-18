# From a CSV file, read each entry for (username : postal_code). Create dictionary of (username : postal_code)
# From garden_address and postal_code, get distance between postal_code and garden.
# Create and return dictionary of (username : distance)

import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def address_to_distance() -> dict():
    return {"user1": 3.1415, "user2": 1.618}


def read_excel_data_to_dict(filename: str = os.getenv("FILENAME", "DEFAULT")) -> dict():
    try:
        data_frame = pd.read_excel(filename)
        return dict(zip(data_frame[data_frame.columns[0]], data_frame[data_frame.columns[1]]))
    except FileNotFoundError:
        print("File not found")
        print(FileNotFoundError.with_traceback())
    except Exception as e:
        print("Unknown exception")
        print(e.with_traceback())
    return {}

# pip install pandas
# pip install python-dotenv
