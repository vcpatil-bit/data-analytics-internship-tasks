# Data Quality Checklist

Run the notebook to populate exact counts; do not enter estimated numbers manually.

| Check | Rule / treatment | Result |
|---|---|---|
| Source and date range | Record source URL and min/max date | Generated in notebook |
| Missing values | Profile by column; do not blanket-fill with zero | Generated in notebook |
| Duplicate records | Check duplicate location-date pairs | Must be 0 after preparation |
| Date parsing | Parse invalid dates as missing, then remove invalid date rows | Applied |
| Numeric types | Convert selected measures to numeric with invalid values coerced to missing | Applied |
| Negative daily counts | Flag as potential official data corrections; do not silently discard | Discuss in interpretation |
| Rolling average | 7-day window, minimum 4 observations | Applied |
| Population-based rates | Use source-provided per-million measures when available | Used where available |
| Aggregate locations | Exclude locations with missing continent from country-only rankings | Applied to ranking |
| Reproducibility | Save raw file and cleaned subset, plus code | Applied on run |

**Important:** Data completeness varies by metric and country. The source's latest observation date can differ by metric and location.
