from datetime import datetime

import pandas as pd

# Load
csv_file_path = './Games_Info_Datasets/merged-game-data-csv-files.csv'
modified_csv_file_path = './Games_Info_Datasets/cleaned-merged-game-data-csv-files.csv'
df = pd.read_csv(csv_file_path)

# Convert 'release_date' to the correct DATE format if necessary
def correct_date_format(date_str):
    try:
        return datetime.strptime(date_str, '%d-%b').strftime('%Y-%m-%d')
    except ValueError:
        return date_str

# Apply corrections
df['release_date'] = df['release_date'].apply(lambda x: correct_date_format(x) if pd.notnull(x) else None)

# Convert 'is_free' to boolean
df['is_free'] = df['is_free'].astype(bool)

# Ensure 'appid' is int
df['appid'] = df['appid'].astype(int)


# Save the modified DataFrame to a new CSV
df.to_csv(modified_csv_file_path, index=False)
