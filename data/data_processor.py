import pandas as pd

# 1. Define the paths to your 3 CSV files 
# (Check your 'data' folder and update these filenames if they differ!)
file_paths = [
    './data/daily_sales_data_0.csv',
    './data/daily_sales_data_1.csv',
    './data/daily_sales_data_2.csv'
]

# Read and combine all three CSV files into a single DataFrame
dataframes = [pd.read_csv(file) for file in file_paths]
df = pd.concat(dataframes, ignore_index=True)

# 2. Filter the rows to keep only "Pink Morsels"
# We use str.lower() just in case there are variations like "Pink morsel" or "PINK MORSEL"
df = df[df['product'].str.lower() == 'pink morsel']

# 3. Clean the 'price' column by removing the '$' and converting it to a float
df['price'] = df['price'].astype(str).str.replace('$', '').astype(float)

# 4. Create the 'sales' column (quantity * price)
df['sales'] = df['quantity'] * df['price']

# 5. Keep only the requested fields: Sales, Date, Region
final_df = df[['sales', 'date', 'region']]

# 6. Save the formatted output to a single CSV file
final_df.to_csv('formatted_sales_data.csv', index=False)

print("Data processing complete! The file 'formatted_sales_data.csv' has been created.")