# Task 24 – Data Quality Audit

## Project Overview

This project focuses on performing a **Data Quality Audit** on the Superstore Sales dataset using Python and Pandas.

The objective was to identify and quantify common data quality issues such as missing values, duplicate records, invalid numerical values, incorrect date values, and categorical inconsistencies.


## Objective

To create a **repeatable data quality checklist** that can be applied to a sales dataset before performing further analysis.



## Tools & Technologies

- Python
- Pandas
- NumPy
- Jupyter Notebook


## Dataset Information

**Dataset:** Superstore Sales Dataset

Total Records: 10,194
Total Columns: 21
Missing Values: 0
Duplicate Records: 0
---

## 🔍 Data Quality Checks Performed

Missing Values — No missing values — 0 issues — PASS
Duplicate Records — No duplicate rows — 0 issues — PASS
Sales Range — Sales should be greater than or equal to 0 — 0 issues — PASS
Quantity Range — Quantity should be greater than 0 — 0 issues — PASS
Discount Range — Discount should be between 0 and 1 — 0 issues — PASS
Order Date Validity — Valid datetime values — 0 issues — PASS
Ship Date Validity — Valid datetime values — 0 issues — PASS
Categorical Consistency — Consistent categorical values — 0 issues — PASS


##  Final Audit Results

- **Total Validation Checks:** 8
- **Passed Checks:** 8
- **Issues Found:** 0
- **Missing Values:** 0
- **Duplicate Records:** 0
- **Invalid Sales Values:** 0
- **Invalid Quantity Values:** 0
- **Invalid Discount Values:** 0
- **Invalid Order Dates:** 0
- **Invalid Ship Dates:** 0
- **Categorical Consistency Issues:** 0


##  Data Cleaning

Since the dataset passed all validation checks:

- No records were removed.
- No missing values required imputation.
- No duplicate records required deletion.
- No numerical values required correction.
- No date values required correction.
- No categorical standardization was required.

A cleaned copy of the dataset was created for downstream analysis.


