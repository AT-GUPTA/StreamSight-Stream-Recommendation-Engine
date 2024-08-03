import pandas as pd

# Load
file_path = './Preprocessed/chunk_1.csv'
df = pd.read_csv(file_path, low_memory=False)

# convert to int
def safe_convert_to_int(value, col_name):
    try:
        if pd.isna(value) or value == "":
            return None
        converted_value = int(float(value))
        if float(value) != converted_value:
            print(f"Non-integer found in {col_name}: {value}")
        return converted_value
    except ValueError as e:
        print(f"Error converting value in {col_name} - '{value}': {e}")
        return None

# convert to boolean
def convert_to_bool(value):
    if pd.isna(value) or value == "":
        return None
    if value in ['True', 'true', '1']:
        return True
    elif value in ['False', 'false', '0']:
        return False
    else:
        print(f"Non-boolean value encountered: {value}")
        return None

# Apply the conversion to integer and boolean columns
integer_columns = ['last_played', 'timestamp_created', 'timestamp_updated']
boolean_columns = ['steam_purchase', 'written_during_early_access']

for col in integer_columns:
    df[col] = df[col].apply(lambda x: safe_convert_to_int(x, col))

for col in boolean_columns:
    df[col] = df[col].apply(convert_to_bool)

# Save the cleaned data
cleaned_file_path = 'clean_new_chunk_1.csv'
df.to_csv(cleaned_file_path, index=False)

# Check data types and any non-integer/non-boolean values
print("Data types after conversion:")
print(df.dtypes)