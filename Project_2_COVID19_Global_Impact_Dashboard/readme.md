# Project 2: COVID-19 Global Impact Dashboard

## Objectives
- Clean daily country-level time-series data.
- Compare case and death trends across countries and time periods.
- Calculate 7-day rolling averages, case-fatality ratio (CFR), and doubling time where meaningful.
- Compare vaccination rollout while clearly documenting missingness and reporting limitations.
- Communicate findings through charts and an interactive dashboard.

## Dataset
Primary source: Our World in Data (OWID), COVID-19 dataset.  
Dataset URL: https://covid.ourworldindata.org/data/owid-covid-data.csv  
The notebook downloads the dataset when run. A network connection is required for the first run. OWID notes that the older GitHub repository stopped updating on 19 August 2024; the stable `covid.ourworldindata.org` URL is used here.

**Attribution:** Our World in Data, COVID-19 dataset. Data is available under the Creative Commons BY license; credit the source when sharing. Review the source documentation for variable definitions and caveats.

## Folder structure
```text
Project_2_COVID19_Global_Impact_Dashboard/
├── data/
│   ├── raw/                 # Downloaded source CSV (created on first notebook run)
│   └── cleaned/             # Cleaned analysis subset (created on first notebook run)
├── notebooks/
│   └── Project_2_COVID19_Global_Impact_Dashboard.ipynb
├── src/
│   └── analysis.py          # Reusable cleaning and KPI functions
├── dashboard/
│   └── app.py               # Streamlit interactive dashboard
├── reports/
│   ├── Project_2_Report.docx
│   ├── Executive_Summary.pdf
│   └── data_quality_checklist.md
├── outputs/                 # Charts and summary tables created by notebook
├── requirements.txt
├── LinkedIn_Post.txt
└── README.md
```

## Analytical definitions
- **7-day rolling average:** mean of the current and previous six daily observations. It smooths reporting noise; it does not remove under-reporting.
- **Case-fatality ratio (CFR):** cumulative reported deaths / cumulative reported cases × 100. It is not an infection-fatality rate and is affected by testing, reporting delays, and case definitions.
- **Approximate doubling time:** ln(2) / slope of ln(cumulative cases) over a recent window, only where the fitted growth rate is positive. Treat as an exploratory estimate, not a forecast.
- **Per-million rates:** values divided by population and multiplied by one million, where population is available and positive.

## Quality and responsible interpretation
- Missing values are retained as missing unless a documented calculation requires otherwise; missing is not automatically zero.
- Negative daily changes can arise from official data corrections. The notebook flags these rather than silently deleting them.
- Comparisons should use rates per million and similar date windows, not raw totals alone.
- Reported cases/deaths vary with testing, definitions, and reporting cadence. Do not infer causation from country-level correlations.
- This project is educational analysis, not medical or policy advice.



