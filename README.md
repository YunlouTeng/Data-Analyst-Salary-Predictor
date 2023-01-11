## Data Science Salary Predictor: Project Overview
* **Goal**: Creating a salary predictor for data science positions to help job seekers understand the job market and make informed career and salary decisions.

* **Impact**

* **Challenges**
  * This project was faced with the challenge of data scraping, as access to Glassdoor API was not available. To collect the most current and fresh data, web scraping techniques using Python were employed, yielding a total of 10,000 pieces of data. However, after data cleaning, only 1,200 pieces of data remained for analysis.
  
  * As the target variable of the regression model, salary data was obtained from the Glassdoor website. However, it should be noted that some of the salary data is estimated by the employer, while some is estimated by Glassdoor. As a result, there may be an issue with potential overestimation of salary data.

* **Interesting findings**

  * Location is an important factor in determining salary for both data scientists and data analysts, with cities such as San Francisco, New York, and Seattle offering the highest salaries.

  * Experience is also a key factor in predicting salary for both data scientists and data analysts, with more experienced professionals earning higher salaries.


## Code and Resources Used
**Python Version** 3.7

**Modules** numpy, pandas, sklearn, matplotlib, seaborn, urllib, beautifulsoup, selenium

**Scraper Github**: 

## Project Summary

Scraped over 1000 job post data from glassdoor using beautifulsoup and selenium modules in python
Feature engineered from the job description text data to distill and quantify 

