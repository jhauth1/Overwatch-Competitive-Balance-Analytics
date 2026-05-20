# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import glob
import os
import re

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    folder_path = r"D:\Documents\Pycharm\Overwatch data cleaner\OverwatchData"
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    df_list = []

    for file in csv_files:

        # Read csv
        df = pd.read_csv(file)

        # Get filename only
        filename = os.path.basename(file)

        # Extract season number from filename
        # Example: ow2_season_03_FINAL...
        match = re.search(r"season_(\d+)", filename)

        if match:
            season_number = int(match.group(1))
        else:
            season_number = 0

        # Add new categorical column
        df["Season"] = season_number

        # Add dataframe to list
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    output_path = os.path.join(folder_path, "cleanedOverwatchData.csv")
    combined_df.to_csv(output_path, index=False)

    print("finished")
    print(f"Exported to: {output_path}")


