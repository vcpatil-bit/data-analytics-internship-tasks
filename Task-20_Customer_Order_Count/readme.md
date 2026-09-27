# Task 20 – Customer Order Count

## Objective
Count unique orders per customer and identify frequent buyers.

## Data logic
The Sample Superstore dataset is transaction-line based. A single Order ID can appear on multiple rows, so order frequency must use **distinct Order IDs** grouped by Customer ID.

## Excel
The workbook uses Excel 365 dynamic-array formulas:
- `UNIQUE()` to identify unique customers/orders
- `FILTER()` to select orders for a customer
- `COUNTA()` to count unique orders
- `XLOOKUP()` to retrieve Customer Name
- `SORT()` / `TAKE()` for Top 10 customers
- `COUNTIF()` for buyer-type summary

## SQL
```sql
SELECT
    Customer_ID,
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS Order_Count
FROM SalesData
GROUP BY Customer_ID, Customer_Name
ORDER BY Order_Count DESC;
```
