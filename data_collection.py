#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:08:55 2022

@author: lavine
"""
import os
import glob
import pandas as pd
#web scraping
from web_scraper import extract_listing




######import all the data analyst job information######
da_file_path = 'URLs/Data_Analyst'
da_csv_files = glob.glob(os.path.join(da_file_path, "*.csv"))

  
# loop over the list of csv files
for f in da_csv_files:
    # read the csv file
    da_df = pd.read_csv(f)
    

######import all the data scientist job information######
ds_file_path = 'URLs/Data_scientist'
ds_csv_files = glob.glob(os.path.join(ds_file_path, "*.csv"))

  
# loop over the list of csv files
for f in ds_csv_files:
    # read the csv file
    ds_df = pd.read_csv(f)


######import all the business intelligence analyst job information######
bia_file_path = 'URLs/Business_Intelligence_Analyst'
bia_csv_files = glob.glob(os.path.join(bia_file_path, "*.csv"))

  
# loop over the list of csv files
for f in bia_csv_files:
    # read the csv file
    bia_df = pd.read_csv(f)


#drop duplicates
da_df2 = da_df.drop_duplicates(subset='joburl')
ds_df2 = ds_df.drop_duplicates(subset='joburl')
bia_df2 = bia_df.drop_duplicates(subset='joburl')


#creating dataframes
data_analyst = []
data_scientist = []
business_intelligence_analyst = []

for joblink in da_df2['joburl']:
    data_analyst.append(extract_listing(joblink))

for joblink in ds_df2['joburl']:
    data_scientist.append(extract_listing(joblink))
    
for joblink in bia_df2['joburl']:
    business_intelligence_analyst.append(extract_listing(joblink))


df_data_analyst = pd.DataFrame(data_analyst,
                               columns = ['CompanyName','company_starRating','CompanyOfferedRole','CompanyRoleLocation','ListingJobDesc','RequestedUrl','YearFounded','CompanySize','CompanyIndustry','CompanyType','CompanySector','CompanyRevenue'])

df_data_scientist = pd.DataFrame(data_scientist,
                               columns = ['CompanyName','company_starRating','CompanyOfferedRole','CompanyRoleLocation','ListingJobDesc','RequestedUrl','YearFounded','CompanySize','CompanyIndustry','CompanyType','CompanySector','CompanyRevenue'])

df_business_intelligence_analyst = pd.DataFrame(business_intelligence_analyst,
                               columns = ['CompanyName','company_starRating','CompanyOfferedRole','CompanyRoleLocation','ListingJobDesc','RequestedUrl','YearFounded','CompanySize','CompanyIndustry','CompanyType','CompanySector','CompanyRevenue'])





dff.to_csv('/Users/lavine/Documents/Terriers!/github/ds_salary/src/file2.csv', index=False)

































