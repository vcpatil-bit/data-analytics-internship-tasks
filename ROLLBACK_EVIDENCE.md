# Task 1 – Rollback Evidence

## Purpose

Git version control is used to maintain previous versions of the data-cleaning project and provide a way to restore a known working version if a future change causes an issue.

## Current Working Version

The GitHub Actions workflow `Data Cleaning Validation` successfully executed the data-cleaning process on the `main` branch.

The successful workflow run completed the following steps:

- Checkout repository
- Set up Python
- Install dependencies
- Run data cleaning script
- Complete job

## Version-Control Evidence

The `src/clean_data.py` file has Git history showing its tracked version.

- File: `src/clean_data.py`
- Commit: `9822ee8`
- Commit message: `Add files via upload`
- Branch: `main`

The Git history provides a recoverable version of the cleaning script.

## Rollback Procedure

If a future modification introduces an error, the project can be restored to a previously known version using Git.

Example procedure:

```bash
git log --oneline
git checkout <known-good-commit>

## Task 2 – Exploratory Data Analysis (EDA)

- Task 2 notebook: `notebooks/Task_2_EDA_Airbnb_Listings.ipynb`
- Analysis performed using Python, Pandas, Matplotlib, and Seaborn.
- EDA includes summary statistics, missing-value analysis, categorical analysis, price analysis, outlier detection, correlation analysis, and visualizations.
- The Task 2 notebook was committed to the repository after completion.
- Rollback can be performed using the Git history to restore the previous repository version if required.
