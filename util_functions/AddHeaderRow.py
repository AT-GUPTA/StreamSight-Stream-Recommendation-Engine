import csv
import os

# header column names
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

input_directory = './Preprocessed/split' 
output_directory = './Preprocessed'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename)

        # Read
        with open(input_file_path, 'r', newline='', encoding='ISO-8859-1') as input_file:
            reader = csv.reader(input_file)
            rows = list(reader)

        # Write
        with open(output_file_path, 'w', newline='', encoding='ISO-8859-1') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)  # Write header
            writer.writerows(rows)  # Write content

print("Header added to all CSV files.")