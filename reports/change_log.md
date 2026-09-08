# Task 1 – Data Cleaning Change Log

| Data Quality Check | Finding | Action Taken |
|---|---|---|
| Missing values | 0 missing values | No action required |
| Complete duplicate rows | 0 duplicates | No rows removed |
| Row ID | 0 duplicate IDs | No action required |
| Order ID | 5,083 repeated IDs | Retained because one order can contain multiple line items |
| Data types | Appropriate | No conversion required |
| Categorical values | No obvious inconsistencies | No correction required |
| Leading/trailing spaces | None found | No correction required |
| Sales | No negative or zero values | No correction required |
| Quantity | No negative or zero values | No correction required |
| Discount | No negative values or values above 100% | No correction required |
| Date validation | 0 Ship Dates before Order Dates | No correction required |
| Outliers | IQR identified potential outliers | Reviewed and retained because values can represent legitimate transactions |
| Profit | Negative values present | Retained because negative profit can represent genuine business losses |

## Final Cleaning Result

- Original rows: 10,194
- Cleaned rows: 10,194
- Rows removed: 0
- Columns: 21

The cleaned dataset was exported as CSV and XLSX.