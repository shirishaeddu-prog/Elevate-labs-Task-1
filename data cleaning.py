import pandas as pd

# -----------------------------
# DATASET
# -----------------------------

data = {
    "Customer ID": [101, 102, 103, 104, 105, 106, 107, 107, 108, 109, 110, 111],
    "Customer Name": [
        "Alice", "Bob", " Charlie ", "Diana",
        "Ethan", "Fiona", "George", "George",
        "Hannah", "Ivy", "Jack", "Kiran"
    ],
    "Age": [25, 31, None, 28, "35", 22, 40, 40, 29, "27", 33, None],
    "Gender": [
        "female", "Male", "M", "FEMALE",
        "male ", None, "Male", "Male",
        "female", "F", "MALE", "female"
    ],
    "Country": [
        "india", "INDIA", "India ", "india",
        "USA", "usa", "India", "India",
        " UK ", "uk", "Usa", "INDIA"
    ],
    "Sale Date": [
        "01/09/2026", "2026-09-02", "03-09-2026",
        "09/04/2026", "2026/09/05", "06-09-2026",
        "07/09/2026", "07/09/2026", "2026-09-08",
        "09/09/2026", "10-09-2026", "11/09/2026"
    ],
    "Sales Amount": [
        1200, 1500, 1100, 1750, 2000, None,
        1300, 1300, 1600, 1450, 1550, 1250
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)

# -----------------------------
# DATA CLEANING
# -----------------------------

# 1. Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Clean customer names
df["customer_name"] = (
    df["customer_name"]
    .astype("string")
    .str.strip()
    .str.title()
)

# 4. Standardize gender
df["gender"] = (
    df["gender"]
    .astype("string")
    .str.strip()
    .str.lower()
)

df["gender"] = df["gender"].replace({
    "m": "male",
    "f": "female"
})

# Fill missing gender
df["gender"] = df["gender"].fillna("unknown")

# 5. Standardize country
df["country"] = (
    df["country"]
    .astype("string")
    .str.strip()
    .str.title()
)

df["country"] = df["country"].replace({
    "Usa": "USA",
    "Uk": "UK"
})

# 6. Convert Age to number
df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)

# Fill missing age with median
df["age"] = df["age"].fillna(
    df["age"].median()
)

# 7. Convert Sales Amount to number
df["sales_amount"] = pd.to_numeric(
    df["sales_amount"],
    errors="coerce"
)

# Fill missing sales amount
df["sales_amount"] = df["sales_amount"].fillna(
    df["sales_amount"].median()
)

# 8. Convert date format
df["sale_date"] = pd.to_datetime(
    df["sale_date"],
    errors="coerce",
    dayfirst=True
)

# -----------------------------
# FINAL CLEANED DATA
# -----------------------------

print("\nCLEANED DATA")
print(df)

# Save cleaned data
df.to_csv(
    "cleaned_sales_data.csv",
    index=False
)

df.to_excel(
    "cleaned_sales_data.xlsx",
    index=False
)

print("\n-----------------------------")
print("DATA CLEANING COMPLETED!")
print("-----------------------------")
print("Cleaned CSV: cleaned_sales_data.csv")
print("Cleaned Excel: cleaned_sales_data.xlsx")