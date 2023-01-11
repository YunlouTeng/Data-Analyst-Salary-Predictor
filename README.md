## Data Analyst Salary Predictor: Project Overview
* **Goal**: Creating a salary predictor for data science positions to help job seekers understand the job market and make informed career and salary decisions.

* **Impact**: Lower the RMSE from 0.8 to 0.4 by ensemble methods.

* **Challenges**:
  * To collect the most current and fresh data, web scraping techniques using Python were employed, yielding a total of 10,000 pieces of data. However, after data cleaning, only 1,200 pieces of data remained for analysis.
  
  * Salary data, the target variable for regression model, obtained from Glassdoor, may have overestimation issues as it's estimated by both employers and Glassdoor.

* **Interesting findings**:

  * Location is an important factor in determining salary for both data scientists and data analysts, with cities such as San Francisco, New York, and Seattle offering the highest salaries.

  * Experience is also a key factor in predicting salary for both data scientists and data analysts, with more experienced professionals earning higher salaries.

* **Future work**: Building a client facing API using flask, and intergrate this salary prediction model into [my cover letter generator website](https://yunlouteng-cover-letter-hero.streamlit.app) as a fun feature

## Code and Resources Used
**Python Version** 3.7

**Modules** numpy, pandas, sklearn, matplotlib, seaborn, urllib, beautifulsoup, selenium

**Scraper Github**: https://github.com/kelvinxuande/glassdoor-scraper

## Project Summary

1.Scraped over 1000 job post data from glassdoor using beautifulsoup and selenium modules in python
2.Feature engineered from the job description text data to distill and quantify 

