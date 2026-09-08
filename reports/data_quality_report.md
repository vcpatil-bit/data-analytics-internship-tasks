
# Task 1 – Data Cleaning and Preprocessing

## Dataset
Dataset used: Sample Superstore

Original dataset size: 10,194 rows and 21 columns.

## Data Quality Checks

### 1. Missing Values
No missing/null values were found in any column.

Result: 0 missing values.

Action: No imputation or row removal was required.

### 2. Duplicate Records
No completely duplicated rows were found.

Result: 0 duplicate rows.

Row ID was also unique. Repeated Order IDs were retained because one order can contain multiple product line items.

### 3. Data Types
The dataset contained appropriate data types:
- Order Date and Ship Date: datetime
- Sales, Discount and Profit: float
- Row ID and Quantity: integer
- Categorical and identifier fields: object

Postal Code was retained as an object/string field because it is an identifier rather than a numerical measure.

### 4. Categorical Consistency
Categorical columns were checked for inconsistent values and capitalization.

No obvious inconsistent category values were identified.

### 5. Extra Spaces
Text columns were checked for leading and trailing spaces.

No extra spaces were found.

### 6. Invalid Values
The following checks were performed:
- Negative Sales: 0
- Zero Sales: 0
- Negative Quantity: 0
- Zero Quantity: 0
- Negative Discount: 0
- Discount above 100%: 0

No invalid values were identified.

### 7. Date Validation
Order Date and Ship Date were checked.

No records were found where Ship Date occurred before Order Date.

### 8. Outlier Detection
The IQR method was used to identify potential statistical outliers.

Potential outliers were found in Sales, Quantity, Discount and Profit. These values were reviewed and retained because they can represent legitimate business transactions.

Negative Profit values were also retained because they represent genuine business losses rather than invalid data.

## Cleaning Actions

The following preprocessing actions were applied:
- Created a separate cleaned copy of the raw dataset.
- Removed completely duplicated rows.
- Removed leading/trailing spaces from actual text values.
- Preserved valid business outliers.
- Preserved repeated Order IDs representing multiple line items.

No records were removed because no invalid or duplicate records were identified.

## Final Dataset

Final dataset size: 10,194 rows and 21 columns.

The cleaned dataset was exported as:
- superstore_cleaned.csv
- superstore_cleaned.xlsx
