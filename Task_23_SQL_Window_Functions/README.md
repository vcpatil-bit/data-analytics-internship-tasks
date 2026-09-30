# Task 23 – SQL Window Functions Intro

## Objective
Use SQL Window Functions to perform ranking, comparison, running-total, and customer/category analysis on the Superstore SalesData dataset.

## Dataset
- Records: 10,194
- Columns: 21
- Source: Superstore SalesData
- Database: `DataAnalytics`
- Table: `SalesData`

## Window Functions Covered
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- PARTITION BY
- SUM() OVER()
- AVG() OVER()
- LAG()
- LEAD()

## Business Questions
1. Which products have the highest sales?
2. How does ROW_NUMBER differ from RANK and DENSE_RANK?
3. Which products rank highest within each category?
4. What is the running total of sales?
5. How do individual product sales compare with category averages?
6. What were the previous and next sales values?
7. Which customers have the highest total sales?
8. What percentage of total sales comes from each category?

## Key Data Analyst Skills
- SQL querying
- Window functions
- Ranking and segmentation
- Customer analysis
- Sales trend analysis
- Business KPI interpretation

## Files
- `Task_23_Window_Functions.sql` – SQL queries
- `Task_23_Report.md` – detailed task report
- `Task_23_Interview_QA.md` – interview questions and answers
- `SalesData_Task23_Import.sql` – SQL import script for the 10,194-row dataset

## How to Run
1. Create/select the `DataAnalytics` database.
2. Ensure the `SalesData` table contains the dataset.
3. Open `Task_23_Window_Functions.sql` in MySQL Workbench.
4. Execute queries section by section.
5. Save screenshots of important outputs for your GitHub evidence.

## GitHub Suggested Folder
`Task_23_SQL_Window_Functions/`
