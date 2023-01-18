# From a CSV file, read each entry for (username : postal_code). Create dictionary of (username : postal_code)
# From garden_address and postal_code, get distance between postal_code and garden.
# Create and return dictionary of (username : distance)

import pandas as pd


def address_to_distance() -> dict():
    return {"user1": 3.1415, "user2": 1.618}


dataframe1 = pd.read_excel('OneNorthPark_Application list.xlsx')
print(dataframe1)
