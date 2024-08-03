import pandas as pd
import psycopg2

# Database connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres.ginzslrkqduexwkazszd",
    "password": "AReallyStrongData5",
    "host": "aws-0-us-west-1.pooler.supabase.com"
}


# Connect to db
conn = psycopg2.connect(**db_params)

# Fetch existing recommendationids
cur = conn.cursor()
cur.execute("SELECT recommendationid FROM steam_reviews;")
existing_ids = cur.fetchall()
existing_ids = set(str(item[0]) for item in existing_ids)
cur.close()
conn.close()

# Load file
csv_file_path = './Preprocessed/merged-csv-files.csv'
df = pd.read_csv(csv_file_path, dtype={'recommendationid': str}, low_memory=False)

# Filter out rows with recommendationids that are not in the db
missing_df = df[~df['recommendationid'].isin(existing_ids)]

# Convert integer fields safely
def safe_int_convert(x):
    try:
        return str(int(float(x)))
    except:
        return x

integer_fields = ['recommendationid', 'appid', 'steamid', 'num_games_owned', 'num_reviews', 'playtime_forever', 'playtime_last_two_weeks', 'playtime_at_review', 'last_played', 'timestamp_created', 'timestamp_updated', 'votes_up', 'votes_funny', 'comment_count']
for field in integer_fields:
    missing_df.loc[:, field] = missing_df[field].apply(safe_int_convert)

# Save
missing_csv_file_path = 'missing_csv_file.csv'
missing_df.to_csv(missing_csv_file_path, index=False)

print(f"Missing CSV saved to {missing_csv_file_path}.")