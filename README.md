## Data Science Salary Predictor: Project Overview
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

**Scraper Github**: 

## Project Summary

Scraped over 1000 job post data from glassdoor using beautifulsoup and selenium modules in python
Feature engineered from the job description text data to distill and quantify 

Web Scraping

Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

Job title
Salary Estimate
Job Description
Rating
Company
Location
Company Headquarters
Company Size
Company Founded Date
Type of Ownership
Industry
Sector
Revenue
Competitors
Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

Parsed numeric data out of salary
Made columns for employer provided salary and hourly wages
Removed rows without salary
Parsed rating out of company text
Made a new column for company state
Added a column for if the job was at the company’s headquarters
Transformed founded date into age of company
Made columns for if different skills were listed in the job description:
Python
R
Excel
AWS
Spark
Column for simplified job title and Seniority
Column for description length
EDA

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

alt text alt text alt text

Model Building

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

Multiple Linear Regression – Baseline for the model
Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.
Model performance

The Random Forest model far outperformed the other approaches on the test and validation sets.

Random Forest : MAE = 11.22
Linear Regression: MAE = 18.86
Ridge Regression: MAE = 19.67
