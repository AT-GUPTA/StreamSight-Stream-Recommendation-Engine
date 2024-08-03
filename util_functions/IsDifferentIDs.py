import pandas as pd

csv_file_path1 = './steam_reviews_2_from_supabase.csv'
csv_file_path2 = './steam_reviews_2_from_supabase.csv'

df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)

all_different = set(df1['recommendationid']).isdisjoint(set(df2['recommendationid']))

print("All recommendationid values are different between the two CSV files:" , all_different)
