import os

import pandas as pd


def read_all_csv(folder_path):
    all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    combined_csv_data = pd.DataFrame()

    for file in all_files:
        file_path = os.path.join(folder_path, file)
        print(f"Processing file: {file}...")
        try:
            csv_data = pd.read_csv(file_path)
            combined_csv_data = pd.concat([combined_csv_data, csv_data])
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    return combined_csv_data

folder_path = './Datasets'
combined_data = read_all_csv(folder_path)
combined_data.to_csv('./combined_csv.csv', index=False)