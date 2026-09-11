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
---

# Task 2 – Exploratory Data Analysis (EDA)

## Project Overview

This project focuses on Exploratory Data Analysis (EDA) of an Airbnb Listings dataset from New York City.

The objective is to understand the dataset, identify patterns and relationships, detect potential outliers, and generate meaningful insights using Python, Pandas, Matplotlib, and Seaborn.
## Dataset Source

The Airbnb Listings dataset was obtained from Inside Airbnb and used for educational exploratory data analysis.

Source: Inside Airbnb – Explore the Data
## Dataset

- Dataset: Airbnb Listings – New York City
- Records: 30,234 listings
- Columns: 90

## EDA Performed

- Dataset structure and data types
- Missing-value analysis
- Duplicate-record check
- Numerical summary statistics
- Categorical data analysis
- Price data cleaning and analysis
- Distribution analysis using histograms
- Room-type price comparison
- Neighbourhood price comparison
- Outlier detection using the IQR method
- Correlation analysis using a heatmap
- Relationship analysis using scatter plots
- Time-based analysis using a line chart

## Key Findings

1. Airbnb prices are right-skewed, with most listings concentrated at lower-to-moderate prices.
2. Hotel rooms have the highest average price among the room types in this dataset.
3. Accommodation capacity has a moderate positive correlation with price (0.47).

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Notebook

The complete EDA analysis is available in:

`notebooks/Task_2_EDA_Airbnb_Listings.ipynb`
# Task 3 – Simple Sales Dashboard Design

## Objective

To create an interactive sales dashboard using the Superstore dataset to monitor sales performance across time, regions, product categories, and top-selling products.

## Tools Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Microsoft Excel
- PivotTables
- PivotCharts
- Slicers

## Key Performance Indicators

- Total Sales: ₹2,326,534.35
- Total Profit: ₹292,296.81
- Total Units Sold: 38,654
- Profit Margin: 12.56%

## Dashboard Visualizations

1. Monthly Sales Trend
2. Sales by Region
3. Sales by Product Category
4. Top 10 Products by Sales

## Interactive Filters

- Region
- Month

## Key Insights

- The West region generated the highest overall sales.
- Technology was the highest-selling product category.
- Monthly sales showed considerable variation across the analyzed period.
- Some products generated negative profit despite having sales, indicating potential pricing or discount-related issues.
- The interactive slicers allow users to analyze sales performance by region and month.

## Deliverables

- Jupyter Notebook containing the analysis
- Excel interactive sales dashboard
- Dashboard supporting PivotTables and PivotCharts
- ## Interview Questions

### 1. How do you decide which KPIs belong on a dashboard vs. in a detailed report?

I select KPIs based on the business objective and the decisions the user needs to make quickly.

A dashboard should contain a small number of important KPIs that provide an immediate overview, such as Total Sales, Total Profit, Units Sold, and Profit Margin.

Detailed reports can contain supporting metrics, detailed tables, calculations, and transaction-level information for deeper analysis.

For this Task 3 dashboard, I selected Total Sales, Total Profit, Total Units Sold, and Profit Margin because they provide a quick view of overall sales performance.

### 2. What makes a dashboard "interactive" rather than just a static chart?

A static chart only displays information and does not allow the user to change the analysis.

A dashboard becomes interactive when users can filter, drill down, or change the view of the data without manually recreating the charts.

In my Task 3 dashboard, I used Excel PivotTables, PivotCharts, and slicers. The Region and Month slicers allow users to filter the dashboard, and the charts update based on those selections.

For example, selecting West from the Region slicer updates the dashboard charts to show the sales performance for the West region.

### 3. How would you design a dashboard differently for an executive vs. an operations manager?

I would design the dashboard based on the user's decision-making needs.

For an executive:
- Focus on high-level KPIs
- Revenue and profit trends
- Profit margin
- Overall business performance
- Important exceptions or alerts
- Simple and clean visual design

For an operations manager:
- Include more operational details
- Regional and category performance
- Product-level performance
- Units sold
- Monthly trends
- 
- # Task 4 – Data Visualization and Storytelling

## Project Overview

This project focuses on transforming the Sample Superstore dataset into an interactive Power BI dashboard and presenting business insights through data visualization and storytelling.

The dashboard follows a clear narrative:

**Context → Problem → Evidence → Recommendation**

## Tool Used

- Power BI Desktop
- Sample Superstore Dataset

## Dashboard Pages

### 1. Executive Overview
Provides a high-level view of:
- Total Sales
- Total Profit
- Total Quantity Sold
- Monthly Sales Performance

### 2. Regional Performance
Analyzes:
- Sales by Region
- Profit by Region
- Profit Margin by Region

### 3. Category & Sub-Category Analysis
Analyzes:
- Sales by Category
- Profit by Category
- Profit by Sub-Category

### 4. Profitability Problem Analysis
Examines:
- Sales vs Profit by Sub-Category
- Average Discount vs Profit

### 5. Business Recommendations
Summarizes key findings and provides actionable recommendations based on the analysis.

## Key Business Insights

- The West region generates the highest sales and profit.
- The Central region has the lowest profit margin.
- Technology is the strongest category in terms of sales and profit.
- Furniture generates substantial sales but comparatively lower profit.
- Some sub-categories generate negative profit.
- Several sub-categories show weak profitability at relatively higher discount levels.

## Business Recommendations

1. Review pricing, discounts, product mix, and operating costs in the Central region.
2. Continue investing in high-performing Technology products while monitoring margins.
3. Analyze Furniture pricing and discounting to improve profitability.
4. Establish discount thresholds for low-margin and loss-making sub-categories.
5. Study successful practices in the West region and evaluate whether they can be applied to other regions.

## Priority Action

Prioritize profitability improvement in the Central region and low-margin sub-categories while maintaining growth in high-performing Technology products.

## Deliverable

The main deliverable is the Power BI report:

`Task_4_Data_Visualization_Storytelling.pbix`
- Underperforming or negative-profit products
- More filters for detailed investigation

In short, an executive dashboard answers "How is the business performing?", while an operations dashboard answers "What is happening and where do I need to take action?"
