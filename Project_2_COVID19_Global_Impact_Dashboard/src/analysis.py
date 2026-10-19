"""Reusable functions for the COVID-19 Global Impact Dashboard project."""
import numpy as np
import pandas as pd

DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
CORE_COLUMNS = [
    "iso_code", "continent", "location", "date", "population",
    "total_cases", "new_cases", "total_deaths", "new_deaths",
    "total_vaccinations", "people_vaccinated", "people_fully_vaccinated",
    "total_cases_per_million", "new_cases_per_million",
    "total_deaths_per_million", "new_deaths_per_million",
    "people_vaccinated_per_hundred", "people_fully_vaccinated_per_hundred"
]

def load_source(path=None):
    """Load a local OWID CSV if supplied; otherwise download the source dataset."""
    if path:
        return pd.read_csv(path, low_memory=False)
    return pd.read_csv(DATA_URL, low_memory=False)

def prepare_data(df):
    """Select useful fields, normalize dates, and sort country timelines."""
    keep = [c for c in CORE_COLUMNS if c in df.columns]
    out = df[keep].copy()
    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    out = out.dropna(subset=["location", "date"])
    numeric = [c for c in out.columns if c not in ["iso_code", "continent", "location", "date"]]
    for col in numeric:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.drop_duplicates(subset=["location", "date"], keep="last")
    out = out.sort_values(["location", "date"]).reset_index(drop=True)
    out["new_cases_7day_avg"] = out.groupby("location")["new_cases"].transform(
        lambda s: s.rolling(7, min_periods=4).mean())
    out["new_deaths_7day_avg"] = out.groupby("location")["new_deaths"].transform(
        lambda s: s.rolling(7, min_periods=4).mean())
    out["case_fatality_ratio_pct"] = np.where(
        out["total_cases"] > 0, out["total_deaths"] / out["total_cases"] * 100, np.nan)
    return out

def latest_country_summary(clean):
    """One latest non-null observation per location for selected metrics."""
    metrics = [c for c in [
        "total_cases", "total_deaths", "total_cases_per_million",
        "total_deaths_per_million", "people_vaccinated_per_hundred",
        "people_fully_vaccinated_per_hundred", "population"
    ] if c in clean.columns]
    rows = []
    for location, group in clean.groupby("location", sort=False):
        row = {"location": location, "date": group["date"].max()}
        for metric in metrics:
            valid = group.loc[group[metric].notna(), ["date", metric]]
            row[metric] = valid.iloc[-1][metric] if not valid.empty else np.nan
        rows.append(row)
    return pd.DataFrame(rows)

def quality_report(raw, clean):
    return {
        "raw_rows": int(len(raw)),
        "raw_columns": int(len(raw.columns)),
        "clean_rows": int(len(clean)),
        "clean_columns": int(len(clean.columns)),
        "duplicate_location_date_after_cleaning": int(clean.duplicated(["location", "date"]).sum()),
        "missing_cells_cleaned": int(clean.isna().sum().sum()),
        "date_min": str(clean["date"].min().date()) if len(clean) else "N/A",
        "date_max": str(clean["date"].max().date()) if len(clean) else "N/A",
    }
