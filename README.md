# Task 1 – Data Cleaning and Preprocessing

## Project Overview

This project focuses on cleaning and preprocessing the Sample Superstore dataset.

The objective is to identify and evaluate common data-quality issues such as missing values, duplicate records, inconsistent values, incorrect data types, invalid values, and outliers.

## Dataset

Dataset: Sample Superstore

- Original rows: 10,194
- Original columns: 21

The original raw dataset is preserved in the data/raw folder.

## Data Quality Checks

- Dataset structure and data types
- Missing values
- Duplicate records
- Numerical summary
- IQR-based outlier detection
- Invalid numerical values
- Categorical consistency
- Leading/trailing spaces
- Date validation
- Row ID and Order ID checks

## Findings

### Missing Values

No missing/null values were found.

### Duplicate Records

No completely duplicated rows were found.

Row IDs were unique. Repeated Order IDs were retained because one order can contain multiple product line items.

### Data Types

The data types were appropriate for the dataset. Order Date and Ship Date were datetime values, numerical fields were appropriately represented, and categorical/identifier fields were stored as object values.

Postal Code was retained as an object because it is an identifier rather than a numerical measure.

### Invalid Values

No negative or zero Sales values were found.

No negative or zero Quantity values were found.

No negative Discount values or Discount values above 100% were found.

No records had a Ship Date earlier than the Order Date.

### Outlier Detection

The IQR method was used to identify potential statistical outliers in Sales, Quantity, Discount and Profit.

The identified observations were reviewed and retained because they can represent legitimate business transactions.

Negative Profit values were retained because they can represent genuine business losses.

## Cleaning Performed

- Created a separate cleaned copy of the raw dataset.
- Checked and removed complete duplicate rows.
- Checked leading/trailing spaces in text values.
- Checked missing values.
- Checked data types.
- Checked invalid numerical values.
- Checked date consistency.
- Identified and reviewed statistical outliers.
- Preserved legitimate business values.

## Cleaning Result

- Original rows: 10,194
- Cleaned rows: 10,194
- Rows removed: 0
- Final dataset: 10,194 rows × 21 columns

## Project Structure

```text
Task_1_Data_Cleaning/
├── README.md
├── data/
│   ├── raw/
│   │   └── sample_-_superstore.xls
│   └── cleaned/
│       ├── superstore_cleaned.csv
│       └── superstore_cleaned.xlsx
├── notebooks/
├── reports/
│   └── data_quality_report.md
└── src/
```

## Output Files

- superstore_cleaned.csv
- superstore_cleaned.xlsx

## Tools Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Excel
- GitHub

## Conclusion

The Sample Superstore dataset was systematically checked for common data-quality issues. No missing values, complete duplicate records, invalid numerical values, categorical inconsistencies, or date-sequence errors were identified. Potential statistical outliers were reviewed and retained because they represented plausible business observations.