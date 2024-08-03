import csv
import os

# header
header = [
    "appid",
    "recommendationid",
    "steamid",
    "num_games_owned",
    "num_reviews",
    "playtime_forever",
    "playtime_last_two_weeks",
    "playtime_at_review",
    "last_played",
    "review",
    "timestamp_created",
    "timestamp_updated",
    "voted_up",
    "votes_up",
    "votes_funny",
    "weighted_vote_score",
    "comment_count",
    "steam_purchase",
    "received_for_free",
    "written_during_early_access"
]

# columns that should be integers
integer_columns = ["appid", "recommendationid", "steamid", "num_games_owned", "num_reviews", "playtime_forever", 
                   "playtime_last_two_weeks", "playtime_at_review", "last_played", "timestamp_created", "timestamp_updated", 
                   "votes_up", "votes_funny", "comment_count"]

# Parameters for processing
input_file_path = './missing_csv_file.csv' # file to be split
lines_per_file = 250000
output_dir = './Preprocessed/split' # directory to save the chunks

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to convert specific columns to integers if they are not NaN
def convert_row_to_integers(row, integer_columns):
    for index, column_name in enumerate(header):
        if column_name in integer_columns:
            try:
                row[index] = int(float(row[index]))
            except ValueError:
                # conversion not possible
                pass
    return row

# Splitting into smaller chunks
def split_csv(input_file_path, lines_per_file, output_dir, header, integer_columns):
    with open(input_file_path, 'r', newline='', encoding='utf-8') as input_file:
        reader = csv.reader(input_file)
        next(reader)  # Skip the original header if it exists
        
        chunk_number = 0
        while True:
            # Create a new file for each chunk
            output_file_path = os.path.join(output_dir, f'db_chunk_{chunk_number}.csv')
            with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header)  # Write header
                
                # Write the specified number of lines per file
                for _ in range(lines_per_file - 1):
                    try:
                        row = next(reader)
                        # Convert specified columns to integers
                        row = convert_row_to_integers(row, integer_columns)
                        writer.writerow(row)
                    except StopIteration:
                        return
                chunk_number += 1

split_csv(input_file_path, lines_per_file, output_dir, header, integer_columns)

print("CSV file has been split into chunks with headers.")
