import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Check df has lat long columns.
# Overwrite excel file with the dataframe. Username, postal code should have no change.
# Only the lat and long columns added.


def write_dataframe_to_excel(df: pd.DataFrame, filename: str, sheetname: str = "Sheet1") -> None:
    with pd.ExcelWriter('/content/gdrive/MyDrive/Colab Notebooks/BallotAlgo/Excel/' + filename, if_sheet_exists='replace', mode='a') as writer:
        workbook = writer.book
        try:
            workbook.remove(workbook[sheetname])
        except:
            print(
                f"Worksheet {sheetname} doesn't exist. Creating new worksheet...")
        finally:
            print(f"Writing to: {filename}, sheet: {sheetname}")
            df.to_excel(writer, sheet_name=sheetname,
                        index=False)
    return
