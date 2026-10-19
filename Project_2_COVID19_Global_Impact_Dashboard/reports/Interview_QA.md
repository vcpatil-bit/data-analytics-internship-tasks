# Project 2 — Interview Questions and Answers

**1. Why did you use a 7-day rolling average?**  
Daily case and death counts can fluctuate because of weekends, delayed reporting, and batch updates. A 7-day rolling average reduces short-term noise and makes broad trends easier to compare. It does not correct under-reporting or remove systematic bias.

**2. What is the case-fatality ratio (CFR), and what are its limitations?**  
CFR is cumulative reported deaths divided by cumulative reported confirmed cases, multiplied by 100. It is not the infection-fatality rate. It can be affected by testing access, case definitions, time lag between diagnosis and outcome, and reporting completeness.

**3. How did you handle missing values?**  
I inspected missingness by column and preserved unknown values rather than replacing every blank with zero. A blank vaccination value, for example, does not prove that no one was vaccinated.

**4. How did you make country comparisons fairer?**  
I used population-based rates per million where available and compared trends over explicit date windows. I also excluded aggregate regions from country-only rankings and documented differences in reporting.

**5. Can the dashboard prove that vaccination reduced deaths?**  
No. This is descriptive analysis. A causal claim would require a suitable study design and control for factors such as age, prior infection, variants, time lags, healthcare capacity, and reporting practices.

**6. What would you improve next?**  
I would add a clear date selector, metric-specific data freshness checks, uncertainty/context notes, automated tests for the cleaning pipeline, and a carefully designed statistical analysis before drawing causal conclusions.
