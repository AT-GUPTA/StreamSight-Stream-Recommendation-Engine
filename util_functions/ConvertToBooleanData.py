import numpy as np
import pandas as pd

# Load
file_path = './Preprocessed/chunk_with_header_1.csv'
df = pd.read_csv(file_path, low_memory=False)

# Clean the boolean columns
boolean_columns = ['voted_up', 'steam_purchase', 'received_for_free', 'written_during_early_access']
for col in boolean_columns:
    df[col] = df[col].apply(lambda x: True if str(x) == 'True' else False if str(x) == 'False' else None)

# Handle columns that are being interpreted as floats when they should be integers
bigint_columns = ['votes_up', 'votes_funny', 'comment_count']
for col in bigint_columns:
    # fill NaN values with -1
    df[col] = df[col].fillna(-1)
    
    # check if there are non-integer values that need handling
    df[col] = np.round(df[col])

    # convert the column to pandas nullable integers
    df[col] = df[col].astype('Int64')

cleaned_file_path = 'cleaned_for_bool_chunk1.csv'
df.to_csv(cleaned_file_path, index=False)