# Task-22 Customer Cohort Retention Analysis

## Project Overview

This project analyzes customer retention behavior using cohort analysis
on the Online Retail II dataset.

Customers are grouped into cohorts based on their first purchase month,
and their subsequent purchasing behavior is analyzed over time.

## Objective

The main objective is to understand customer retention over time and
identify patterns in repeat purchasing behavior.

## Dataset

**Dataset:** Online Retail II

The dataset contains transactional retail data including:

- Invoice
- StockCode
- Description
- Quantity
- InvoiceDate
- Price
- Customer ID
- Country

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Data Cleaning

The following preprocessing steps were performed:

- Removed records with missing Customer IDs
- Removed cancelled invoices
- Removed transactions with invalid quantities
- Removed transactions with invalid prices
- Converted InvoiceDate to datetime
- Created monthly transaction periods

## Methodology

1. Load the Online Retail II dataset.
2. Clean and preprocess the transaction data.
3. Create the transaction month.
4. Identify each customer's first purchase month.
5. Assign customers to monthly cohorts.
6. Calculate the cohort index.
7. Count unique customers for each cohort period.
8. Calculate customer retention percentages.
9. Create a cohort retention table.
10. Visualize retention using a heatmap.
11. Calculate retention metrics.
12. Generate business insights.

## Key Results

- Average One-Month Retention: **20.53%**
- Average Three-Month Retention: **25.19%**
- A cohort retention heatmap was created to visualize customer
  retention across different cohorts and periods.

## Deliverables

- Jupyter Notebook
- Cohort Customer Table
- Cohort Retention Table
- Retention Heatmap
- Business Insights

## Business Insights

Cohort analysis provides a structured way to understand customer
behavior over time.

The analysis shows different retention patterns across customer
cohorts. Newer cohorts have fewer available future periods, resulting
in missing values for later cohort indexes.

The analysis can help businesses understand repeat purchasing behavior
and identify opportunities for customer retention and engagement.

## Conclusion

This project demonstrates the use of Python and data analytics
techniques to analyze customer lifecycle behavior.

The project covers data cleaning, customer segmentation, cohort
analysis, retention calculation, visualization, and business
interpretation.
