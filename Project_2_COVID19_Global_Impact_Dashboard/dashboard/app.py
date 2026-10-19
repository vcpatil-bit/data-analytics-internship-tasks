from pathlib import Path
import sys
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from analysis import load_source, prepare_data, latest_country_summary

st.set_page_config(page_title="COVID-19 Global Impact", layout="wide")
st.title("COVID-19 Global Impact Dashboard")
st.caption("Educational descriptive analysis | Source: Our World in Data")
st.warning("Reported counts are affected by testing, definitions, and reporting practices. Charts do not establish causation.")

local_raw = ROOT / "data" / "raw" / "owid-covid-data.csv"
@st.cache_data(show_spinner="Loading COVID-19 data...")
def get_data():
    if local_raw.exists():
        raw = pd.read_csv(local_raw, low_memory=False)
    else:
        raw = load_source()
        local_raw.parent.mkdir(parents=True, exist_ok=True)
        raw.to_csv(local_raw, index=False)
    return prepare_data(raw)

try:
    df = get_data()
except Exception as exc:
    st.error("Could not load the source dataset. Check your internet connection or place the OWID CSV in data/raw/owid-covid-data.csv.")
    st.exception(exc)
    st.stop()

country_options = sorted(df.loc[df["continent"].notna(), "location"].dropna().unique().tolist())
default = [c for c in ["India", "United States", "Brazil", "United Kingdom"] if c in country_options]
selected = st.sidebar.multiselect("Countries", country_options, default=default[:4] or country_options[:3])
date_min, date_max = df["date"].min().date(), df["date"].max().date()
start_date, end_date = st.sidebar.date_input("Date range", value=(date_min, date_max), min_value=date_min, max_value=date_max)
if not isinstance(start_date, type(date_min)) or not isinstance(end_date, type(date_max)):
    st.info("Choose a start and end date.")
    st.stop()
view = df[(df["location"].isin(selected)) & (df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)].copy()

latest = latest_country_summary(view)
a, b, c = st.columns(3)
a.metric("Countries selected", len(selected))
b.metric("Reported cases (latest selected rows)", f"{latest['total_cases'].sum(min_count=1):,.0f}" if "total_cases" in latest else "N/A")
c.metric("Reported deaths (latest selected rows)", f"{latest['total_deaths'].sum(min_count=1):,.0f}" if "total_deaths" in latest else "N/A")
st.caption("Totals above are a sum of each selected country's latest available cumulative values within the filtered date window; they are not daily totals.")

if view.empty:
    st.warning("No data for the selected filters.")
    st.stop()

tab1, tab2, tab3 = st.tabs(["Cases & deaths", "Vaccination", "Country comparison"])
with tab1:
    fig = px.line(view, x="date", y="new_cases_7day_avg", color="location", title="Daily reported cases — 7-day rolling average")
    st.plotly_chart(fig, use_container_width=True)
    fig2 = px.line(view, x="date", y="new_deaths_7day_avg", color="location", title="Daily reported deaths — 7-day rolling average")
    st.plotly_chart(fig2, use_container_width=True)
with tab2:
    if "people_fully_vaccinated_per_hundred" in view and view["people_fully_vaccinated_per_hundred"].notna().any():
        fig3 = px.line(view, x="date", y="people_fully_vaccinated_per_hundred", color="location",
                       title="People fully vaccinated (% of population, as reported)")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("Vaccination data is not available for the current selection.")
with tab3:
    show = latest_country_summary(view)
    st.dataframe(show.sort_values("total_cases_per_million", ascending=False, na_position="last"), use_container_width=True)
    st.download_button("Download country summary CSV", show.to_csv(index=False).encode("utf-8"),
                       file_name="latest_country_summary.csv", mime="text/csv")
