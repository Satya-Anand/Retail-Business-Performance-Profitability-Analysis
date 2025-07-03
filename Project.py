import pandas as pd

# Load the CSV file
file_path = "C:\\Users\\satya\\Downloads\\Project.csv"  # Update path if needed
df = pd.read_csv(file_path, encoding='latin1')

# Preview the first few rows
print("Before cleaning:")
print(df.head())

# Convert Order Date and Ship Date to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')


# Drop rows with missing values
df = df.dropna()

# Create a 'Season' column based on Order Date
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['Season'] = df['Order Date'].dt.month.apply(get_season)

# Calculate COGS (Cost of Goods Sold) = Sales - Profit
df['COGS'] = df['Sales'] - df['Profit']

# Calculate Profit Margin = Profit / Sales
df['Profit Margin'] = df['Profit'] / df['Sales']

# Calculate Gross Margin = (Sales - COGS) / Sales
df['Gross Margin'] = (df['Sales'] - df['COGS']) / df['Sales']

# Handle divide-by-zero (infinite) and NaN values
df.replace([float("inf"), -float("inf")], 0, inplace=True)
df.fillna(0, inplace=True)

# Export cleaned data to CSV
df.to_csv("Cleaned_Superstore.csv", index=False)

print("✅ Cleaning complete. Cleaned data saved as 'Cleaned_Superstore.csv'")
