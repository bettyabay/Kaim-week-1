import os
import pandas as pd

# Path to the directory containing CSV files
directory_path = "C:/Users/USER/Desktop/KAIM/Kaim-week-1/Data/yfinance_data"

# List to store dataframes
dataframes = []

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory_path, filename)
        # Read CSV file
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Concatenate all dataframes
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_output.csv", index=False)

print("Merged CSV saved as 'merged_output.csv'")
merged_df = pd.read_csv("stock_data.csv", header=0)


