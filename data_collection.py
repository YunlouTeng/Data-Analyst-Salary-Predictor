#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:08:55 2022

@author: lavine
"""

import pandas as pd
from tqdm import tqdm
from read_folder import read_folder
#web scraping
from web_scraper import extract_listing


#input data
da_df = read_folder('URLs/Data_Analyst')

ds_df = read_folder('URLs/Data_scientist')

bia_df = read_folder('URLs/Business_Intelligence_Analyst')

print(da_df.shape)
print(ds_df.shape)
print(bia_df.shape)

#drop duplicates
da_df2 = da_df.drop_duplicates(subset='joburl')
ds_df2 = ds_df.drop_duplicates(subset='joburl')
bia_df2 = bia_df.drop_duplicates(subset='joburl')

print(da_df2.shape)
print(ds_df2.shape)
print(bia_df2.shape)

#web scraping
data_analyst = []
data_scientist = []
business_intelligence_analyst = []

for joblink in tqdm(da_df2['joburl']):
    data_analyst.append(extract_listing(joblink))

for joblink in tqdm(ds_df2['joburl']):
    data_scientist.append(extract_listing(joblink))
    
for joblink in tqdm(bia_df2['joburl']):
    business_intelligence_analyst.append(extract_listing(joblink))


df_data_analyst = pd.DataFrame(data_analyst,
                               columns = ['CompanyName','company_starRating','CompanyOfferedRole','CompanyRoleLocation','ListingJobDesc','RequestedUrl','YearFounded','CompanySize','CompanyIndustry','CompanyType','CompanySector','CompanyRevenue'])

df_data_scientist = pd.DataFrame(data_scientist,
                               columns = ['CompanyName','company_starRating','CompanyOfferedRole','CompanyRoleLocation','ListingJobDesc','RequestedUrl','YearFounded','CompanySize','CompanyIndustry','CompanyType','CompanySector','CompanyRevenue'])

df_business_intelligence_analyst = pd.DataFrame(business_intelligence_analyst,
                               columns = ['CompanyName','company_starRating','CompanyOfferedRole','CompanyRoleLocation','ListingJobDesc','RequestedUrl','YearFounded','CompanySize','CompanyIndustry','CompanyType','CompanySector','CompanyRevenue'])


#add est. salary
df_data_analyst = df_data_analyst.merge(da_df2, how ='inner', left_on = ['RequestedUrl'],right_on = ['joburl'])
df_data_analyst = df_data_analyst[['CompanyName', 'company_starRating', 'CompanyOfferedRole','salary','CompanyRoleLocation', 'ListingJobDesc', 'RequestedUrl', 'YearFounded','CompanySize', 'CompanyIndustry', 'CompanyType', 'CompanySector','CompanyRevenue']]

df_data_scientist = df_data_scientist.merge(da_df2, how ='inner', left_on = ['RequestedUrl'],right_on = ['joburl'])
df_data_scientist = df_data_scientist[['CompanyName', 'company_starRating', 'CompanyOfferedRole','salary','CompanyRoleLocation', 'ListingJobDesc', 'RequestedUrl', 'YearFounded','CompanySize', 'CompanyIndustry', 'CompanyType', 'CompanySector','CompanyRevenue']]

df_business_intelligence_analyst = df_business_intelligence_analyst.merge(da_df2, how ='inner', left_on = ['RequestedUrl'],right_on = ['joburl'])
df_business_intelligence_analyst = df_business_intelligence_analyst[['CompanyName', 'company_starRating', 'CompanyOfferedRole','salary','CompanyRoleLocation', 'ListingJobDesc', 'RequestedUrl', 'YearFounded','CompanySize', 'CompanyIndustry', 'CompanyType', 'CompanySector','CompanyRevenue']]

#export the data 
df_data_analyst.to_csv('/Users/lavine/Documents/Terriers!/github/job_analysis_project/data/df_data_analyst.csv', index=False)
df_data_scientist.to_csv('/Users/lavine/Documents/Terriers!/github/job_analysis_project/data/df_data_scientist.csv', index=False)
df_business_intelligence_analyst.to_csv('/Users/lavine/Documents/Terriers!/github/job_analysis_project/data/df_business_intelligence_analyst.csv', index=False)



























