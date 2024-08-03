import os

import pandas as pd

directory = './Datasets'
total_rows = 0

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        try:
            df = pd.read_csv(file_path)
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='ISO-8859-1')
        total_rows += len(df)

print(f"Total number of rows across all CSV files: {total_rows}")
