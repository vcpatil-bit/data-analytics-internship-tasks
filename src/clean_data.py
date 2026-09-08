import pandas as pd

# Load the raw dataset
df = pd.read_excel("../data/raw/sample_-_superstore.xls")

# Create a separate copy for cleaning
df_clean = df.copy()

# Remove completely duplicated rows
df_clean = df_clean.drop_duplicates()

# Remove leading/trailing spaces from actual text values
text_columns = df_clean.select_dtypes(include="object").columns

for col in text_columns:
    df_clean[col] = df_clean[col].map(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# Validate the cleaned dataset
print("Missing values after cleaning:",
      df_clean.isnull().sum().sum())

print("Duplicate rows after cleaning:",
      df_clean.duplicated().sum())

print("Final dataset shape:",
      df_clean.shape)

# Export cleaned files
df_clean.to_csv(
    "../data/cleaned/superstore_cleaned.csv",
    index=False
)

df_clean.to_excel(
    "../data/cleaned/superstore_cleaned.xlsx",
    index=False
)

print("Cleaned CSV and Excel files exported successfully.")