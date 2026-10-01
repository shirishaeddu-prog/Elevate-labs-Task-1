# E# Task 1: Data Cleaning and Preprocessing

## Objective
The objective of this task is to clean and prepare a raw dataset by handling missing values, duplicate records, inconsistent formats, and incorrect data types.

## Tools Used
- Python
- Pandas
- Pydroid 3
- OpenPyXL

## Dataset
The dataset contains customer information such as:
- Customer ID
- Customer Name
- Age
- Gender
- Country
- Sale Date
- Sales Amount

## Data Cleaning Steps

### 1. Column Names
Column names were cleaned and converted into a uniform format using lowercase letters and underscores.

### 2. Duplicate Records
Duplicate rows were identified and removed.

### 3. Missing Values
Missing values were handled:
- Missing Age → replaced with median age
- Missing Sales Amount → replaced with median sales amount
- Missing Gender → replaced with "unknown"

### 4. Text Standardization
- Customer names were cleaned.
- M and F were converted to male and female.
- Country names were standardized.

### 5. Data Types
- Age → Numeric
- Sales Amount → Numeric
- Sale Date → Datetime

### 6. Output Files
The program generates:
- `cleaned_sales_data.csv`
- `cleaned_sales_data.xlsx`

## Result
The original dataset contained 12 rows. After removing the duplicate record, the cleaned dataset contains 11 rows.

## Conclusion
The dataset was successfully cleaned and preprocessed using Python Pandas and is ready for further data analysis.levate-labs-Task-1