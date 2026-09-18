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


 Task 6

Objective

Practice everyday Excel functions used in analyst work:

VLOOKUP

XLOOKUP

IF

SUMIF / SUMIFS

COUNTIF / COUNTIFS

LEFT / MID / RIGHT

LEN / TRIM

INDEX/MATCH

IFERROR

Dataset

Sample Superstore transactional sales data.

The source dataset used in the earlier analysis contains 10,194 rows and covers 2023-01-03 to 2026-12-30. The present Task 6 workbook intentionally uses a smaller practice extract because the task asks for a small transactional dataset.

Workbook Structure

Sheet

Purpose

Start_Here

Task objective, scope and submission checklist

Transactions

Transaction-level data plus live formula columns

Customer_Lookup

Lookup table for VLOOKUP

Product_Lookup

Lookup table for XLOOKUP

Formula_Demo

Live formulas, expected results and usage notes

Summary

Formula-driven summary and coverage

Interview_QA

Interview questions and practical answers

Validation

Edge-case and formula validation tests

Analyst Approach

Kept the transactional structure intact.

Converted dates to real Excel dates.

Added formula-driven business labels instead of hard-coded results.

Used named ranges such as PracticeSales and PracticeProfit.

Tested missing lookup keys and multi-criteria conditions.

Added notes explaining when each function is appropriate.

Quality Checks

Formula cells are live Excel formulas.

Expected results were independently calculated before workbook creation.

Lookup tables use exact matching.

Negative profit rows are retained because they are valid business observations.

High discounts are not automatically treated as errors; they are flagged for review

Interview Question:

What's the difference between SUMIF and SUMIFS?	
SUMIF applies one criterion. SUMIFS supports multiple criteria, so it is useful when an analyst needs a measure filtered by more than one business condition.
How does XLOOKUP improve on VLOOKUP?	
XLOOKUP can return values from either side of the lookup column, uses exact match by default, and can provide a not-found result. It is more flexible for modern Excel work.
When would you use INDEX/MATCH instead of VLOOKUP?	
INDEX/MATCH is useful when the return column is to the left of the lookup column or when a flexible, widely compatible lookup pattern is needed.
What is the risk of text-vs-number mismatches in lookups?	
A value that looks the same can still be stored differently, such as 123 as text versus 123 as a number. This can cause lookups to fail. Check data types and standardize keys before matching.
How do you handle blank cells in formulas?	
Use IF, IFERROR, COUNTBLANK or explicit criteria depending on the business question. Do not silently replace missing values without understanding why they are missing.
Why use named ranges?	
Named ranges make formulas easier to read and maintain. For example, =SUM(PracticeSales) communicates the business meaning more clearly than a long cell reference.

Task 7 – First Chart Story: Turning Numbers into a Narrative
1. Introduction

Data visualization is an important part of data analysis because it helps transform numerical information into clear and meaningful insights. The purpose of this task is to understand how to select an appropriate basic chart for a specific analytical question and communicate the findings through a short data story.

For this task, the Iris dataset was analyzed using Python, Pandas, Matplotlib, and Scikit-learn. Four visualizations were created to compare measurements across the three Iris species: Setosa, Versicolor, and Virginica.

2. Objective

The objectives of this task are:

To understand the structure of a small dataset.
To perform basic aggregation and analysis using Pandas.
To select an appropriate chart type for a given analytical question.
To create clear and labeled visualizations using Matplotlib.
To identify important patterns from the charts.
To convert numerical findings into a meaningful data narrative.
3. Tools and Technologies Used
Tool	Purpose
Python	Programming and analysis
Scikit-learn	Loading the Iris dataset
Pandas	Data manipulation and aggregation
Matplotlib	Data visualization
Jupyter Notebook	Analysis environment
4. Dataset Description

The Iris dataset is a commonly used dataset in data science and machine learning.

It contains:

150 observations
4 numerical features
3 species
Features
Sepal Length
Sepal Width
Petal Length
Petal Width
Species
Setosa
Versicolor
Virginica

Each species contains 50 observations, making the dataset balanced.

5. Loading the Dataset

The Iris dataset was loaded directly from Scikit-learn.

The dataset contains:

150 rows and 5 columns.

The five columns are:

Sepal Length
Sepal Width
Petal Length
Petal Width
Species

The species distribution is:

Species	Number of Observations
Setosa	50
Versicolor	50
Virginica	50
Total	150
Chart 1 – Average Sepal Length by Species
Analytical Question

Which species has the highest average sepal length?

The average sepal length was calculated using Pandas:
Chart Type

Bar Chart

A bar chart was selected because the objective is to compare a numerical value across discrete categories.

Virginica has the highest average sepal length at approximately 6.59 cm, while Setosa has the lowest at approximately 5.01 cm.

Chart 2 – Average Petal Length by Species
Analytical Question

Which species has the longest average petal length?

The average petal length was calculated using:

Chart Type

Bar Chart

The bar chart provides a clear comparison of petal length between the three species.

Virginica has the longest average petal length at approximately 5.55 cm, while Setosa has substantially shorter petals at approximately 1.46 cm.

Chart 3 – Average Sepal and Petal Length by Species
Analytical Question

How do average sepal and petal lengths vary across the three species?

The average values were calculated using:

Chart Type

Line Chart

The line chart was used to visualize the progression of the average measurements across the ordered species categories for this visualization exercise.

Both average sepal and petal lengths increase from Setosa to Virginica, with petal length showing a particularly strong difference between the species.

Chart 4 – Distribution of Iris Species
Analytical Question

Is the dataset balanced across the three species?

The number of observations for each species was calculated using:

Chart Type

Pie Chart

A pie chart was appropriate because there are only three categories and they represent parts of the total dataset.

The Iris dataset is perfectly balanced, with each species representing approximately one-third of the observations.

Summary Analysis
The overall average measurements by species are:

Species	Sepal Length	Sepal Width	Petal Length	Petal Width
Setosa	5.01	3.43	1.46	0.25
Versicolor	5.94	2.77	4.26	1.33
Virginica	6.59	2.97	5.55	2.03

The results show that Virginica generally has the largest measurements, while Setosa has the smallest measurements, particularly for petal dimensions.

The major findings from the analysis are:

Virginica has the highest average sepal length at approximately 6.59 cm.
Virginica has the highest average petal length at approximately 5.55 cm.
Setosa has the smallest petal measurements, making it noticeably different from the other two species.
Petal length shows a strong difference between the three species.
The dataset is perfectly balanced, with 50 records for each species.
Simple visualizations make these differences easier to understand than looking at raw numbers alone.
13. Data Story – Turning Numbers into a Narrative

The Iris dataset contains three equally represented species: Setosa, Versicolor, and Virginica. The analysis reveals clear differences in their physical measurements.

Virginica has the largest average sepal and petal measurements, whereas Setosa has the smallest. The difference is particularly noticeable in petal length, where Virginica averages approximately 5.55 cm compared with only 1.46 cm for Setosa.

The visualizations also show that the average measurements generally increase from Setosa to Virginica. At the same time, the dataset itself is balanced because each species contributes exactly 50 observations.

Therefore, the charts transform the raw numerical measurements into a simple story: the three species have distinct physical characteristics, with Virginica generally being the largest and Setosa the smallest in terms of the measured dimensions.

Interview Questions
Question 1: When would you choose a bar chart over a line chart?
Answer

A bar chart is preferred when comparing values across discrete categories, such as product categories, departments, or species. A line chart is generally better for showing trends or changes across an ordered sequence, especially over time.

Question 2: Why are pie charts often discouraged in professional reporting?
Answer

Pie charts can make it difficult to accurately compare similar-sized segments, especially when there are many categories. Bar charts are usually easier to read and provide more precise comparisons. Pie charts are most useful when there are only a few categories and they represent meaningful parts of a whole.


**Task 8 – Sales Tracker in Google Sheets**

Overview

This project is a lightweight sales tracker built in Google Sheets using a retail sales transaction dataset.

The tracker separates raw transactional data from the summary layer and automatically calculates daily, weekly, and monthly sales and units sold.

Objective

Structure raw retail sales data for ongoing use.

Calculate daily, weekly, and monthly sales automatically.

Apply data validation to reduce incorrect entries.

Verify calculated totals against manual checks.

Provide a dynamic product-category sales visualization.

Dataset

The project uses a retail sales transaction dataset with 1,000 records and fields including:

Transaction ID

Date

Customer ID

Gender

Age

Product Category

Quantity

Price per Unit

Total Amount

Source:
https://github.com/Oragant/Retail-Sales-Dashboard/blob/main/retail_sales_dataset.csv

Workbook Structure

Raw Data

Contains the source transactions plus:

Calculated Amount

Amount Check

Summary

Contains:

Selected Date

Daily Sales

Daily Units Sold

Week Start

Weekly Sales

Weekly Units Sold

Month Start

Monthly Sales

Monthly Units Sold

Manual Daily Sales

Formula Daily Sales

Verification

Dynamic Product Category Sales table

Sales by Product Category chart

Key Formulas

Calculated Amount

=G2*H2

Amount Check

=IF(ROUND(I2,2)=ROUND(J2,2),"PASS","CHECK")

Daily Sales

=SUMIFS('Raw Data'!$I$2:$I$1001,'Raw Data'!$B$2:$B$1001,B3)

Daily Units

=SUMIFS('Raw Data'!$G$2:$G$1001,'Raw Data'!$B$2:$B$1001,B3)

Week Start

=B3-WEEKDAY(B3,2)+1

Weekly Sales

=SUMIFS('Raw Data'!$I$2:$I$1001,'Raw Data'!$B$2:$B$1001,">="&$B$6,'Raw Data'!$B$2:$B$1001,"<"&$B$6+7)

Monthly Sales

=SUMIFS('Raw Data'!$I$2:$I$1001,'Raw Data'!$B$2:$B$1001,">="&$B$9,'Raw Data'!$B$2:$B$1001,"<"&EDATE($B$9,1))

Dynamic Category Sales

=SUMIFS('Raw Data'!$I$2:$I$1001,'Raw Data'!$F$2:$F$1001,D2,'Raw Data'!$B$2:$B$1001,$B$3)
Data Quality

Date formatting standardized.

Currency formatting applied.

Quantity and price validated as positive numbers.

Gender and Product Category use controlled values.

Calculated Amount is compared with Total Amount.

Transaction IDs were checked for uniqueness.

Key fields were checked for missing values.

# Task 9 – Descriptive Statistics Primer

### Objective

The objective of this task is to calculate and interpret descriptive statistics for key numerical variables in the Titanic dataset.

The analysis focuses on understanding:

- Mean
- Median
- Mode
- Standard Deviation
- Percentiles
- Skewness
- Data spread

## Dataset

**Dataset:** Titanic Dataset

The dataset contains information about Titanic passengers, including passenger class, age, family relationships, ticket fare, and other passenger details.

## Tools Used

- Python
- Pandas
- Excel

## Selected Numerical Columns

The following five numerical columns were selected:

1. Age
2. Fare
3. SibSp
4. Parch
5. Pclass

## Descriptive Statistics

Statistic	Age	Fare	SibSp	Parch	Pclass
Count	714	891	891	891	891
Mean	29.70	32.20	0.52	0.38	2.31
Median	28.00	14.45	0.00	0.00	3.00
Mode	24.00	8.05	0.00	0.00	3.00
Standard Deviation	14.53	49.69	1.10	0.81	0.84
25th Percentile	20.13	7.91	0.00	0.00	2.00
50th Percentile	28.00	14.45	0.00	0.00	3.00
75th Percentile	38.00	31.00	1.00	0.00	3.00
<img width="552" height="218" alt="image" src="https://github.com/user-attachments/assets/4343a6cd-979e-41a2-99ac-5b46d12d23e9" />

## Key Findings

### Age

The mean age is 29.70 years and the median is 28.00 years. The mean is slightly higher than the median, suggesting some positive skewness. The middle 50% of ages range from approximately 20.13 to 38.00 years.

### Fare

The mean fare is 32.20 while the median is 14.45. The higher mean suggests positive/right skewness, with higher fare values influencing the average. The standard deviation of 49.69 indicates substantial variability in ticket fares.

### SibSp

The mean is 0.52, while the median and mode are both 0.00. This indicates that having no siblings or spouses aboard was the most common observation.

### Parch

The mean is 0.38, while the median and mode are both 0.00. The 75th percentile is also 0.00, indicating that at least 75% of observations have zero parents or children aboard.

### Pclass

The mean is 2.31, while the median and mode are both 3.00. This indicates that third class is the most frequently occurring passenger class.

## Interview Questions

### 1. When is median a better measure of center than mean?

Median is better when data is skewed or contains extreme values/outliers because it is less affected by unusually high or low observations.

### 2. What does a large standard deviation tell you about a dataset?

A large standard deviation indicates that observations are more widely spread around the mean, showing greater variability in the dataset.

## Files Included

- `Titanic-Dataset.csv` – Dataset used for the analysis
- `Task_9_Descriptive_Statistics.ipynb` – Python/Pandas analysis
- `Task_9_Descriptive_Statistics.xlsx` – Excel statistical summary

# Task 10 – Simple KPI Tracking Sheet

## Tools Used

- Microsoft Excel
- Excel Tables
- Excel Formulas

## Dataset

Sample Superstore Dataset

The dataset contains transactional information including:

- Order ID
- Product Name
- Category
- Sub-Category
- Sales
- Quantity
- Discount
- Profit

## KPIs Created

The KPI Summary contains five key metrics:

1. Total Revenue
2. Units Sold
3. Total Orders
4. Average Order Value
5. Top Product

## KPI Results
SIMPLE KPI TRACKING	
KPI	VALUE
Total Revenue	2327534.35
Units Sold	38664
Total Orders	5111.00
Average Order Value	₹ 455.40
Top Product	Cisco TelePresence System EX90 Videoconferencing Unit

# Task 11 – Basic Data Sorting & Filtering

## Overview

This task focuses on basic data exploration using sorting and filtering
techniques in Microsoft Excel.

## Dataset

Sample Superstore Dataset

## Objective

To practice sorting and filtering and answer simple business questions
using sales, profit, category, region, segment, quantity, and discount data.

## Tools Used

- Microsoft Excel
- GitHub

## Analysis Performed

- Filtered records with Sales greater than $1,000
- Identified records with negative Profit
- Filtered Technology records from the West region
- Filtered Consumer records with Quantity of 5 or more
- Identified records with Discount of 50% or more and negative Profit
- Sorted Sales from largest to smallest

## Business Questions & Results

Business Questions & Answers		
		
Sr. No.	Question	Answer
1	How many records have Sales greater than $1,000?	470
2	How many records have negative Profit?	1901
3	How many Technology records are from the West region?	607
4	How many Consumer records have Quantity of 5 or more?	1602
5	How many records have Discount ≥ 50% and negative Profit?	940

## Key Learnings

- Sorting helps arrange data for easier comparison.
- Filtering helps focus on records meeting specific conditions.
- Multiple filters can be used together to answer business questions.
- Raw data should be preserved rather than permanently deleting records.
- Excel functions such as COUNTIF and COUNTIFS can support filtered analysis.

## Conclusion

This task provided practical experience in basic data sorting and
filtering using Excel and demonstrated how analysts can use simple
business conditions to explore a dataset.
