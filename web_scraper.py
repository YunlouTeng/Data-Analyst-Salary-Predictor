#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 15:24:06 2022

@author: lavine
"""
#web scraping
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup as soup
from selenium import webdriver

#Initializing the webdriver
path = '/Users/lavine/Documents/Terriers!/github/job_analysis_project/chromedriver'
#driver = webdriver.Chrome(path)

# checks and corrects the scheme of the requested url
def checkURL(requested_url):
    if not urlparse(requested_url).scheme:
        requested_url = "https://" + requested_url
    return requested_url


# fetches data from requested url and parses it through beautifulsoup
def requestAndParse(requested_url):
    requested_url = checkURL(requested_url)
    try:
        # define headers to be provided for request authentication
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                        'AppleWebKit/537.11 (KHTML, like Gecko) '
                        'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        request_obj = Request(url = requested_url, headers = headers)
        opened_url = urlopen(request_obj)
        page_html = opened_url.read()
        opened_url.close()
        page_soup = soup(page_html, "html.parser")
        return page_soup, requested_url

    except Exception as e:
        print(e)
        
# extracts desired data from listing banner
def extract_listingBanner(listing_soup):
    listing_bannerGroup_valid = False

    try:
        listing_bannerGroup = listing_soup.find("div", class_="css-ur1szg e11nt52q0")
        listing_bannerGroup_valid = True
    except:
        print("[ERROR] Error occurred in function extract_listingBanner")
        companyName = "NA"
        company_starRating = "NA"
        company_offeredRole = "NA"
        company_roleLocation = "NA"
    
    if listing_bannerGroup_valid:
        try:
            company_starRating = listing_bannerGroup.find("span", class_="css-1pmc6te e11nt52q4").getText()
        except:
            company_starRating = "NA"
        if company_starRating != "NA":
            try:
                companyName = listing_bannerGroup.find("div", class_="css-16nw49e e11nt52q1").getText().replace(company_starRating,'')
            except:
                companyName = "NA"
            # company_starRating.replace("★", "")
            company_starRating = company_starRating[:-1]
        else:
            try:
                companyName = listing_bannerGroup.find("div", class_="css-16nw49e e11nt52q1").getText()
            except:
                companyName = "NA"
            
        try:
            company_offeredRole = listing_bannerGroup.find("div", class_="css-17x2pwl e11nt52q6").getText()
        except:
            company_offeredRole = "NA"

        try:
            company_roleLocation = listing_bannerGroup.find("div", class_="css-1v5elnn e11nt52q2").getText()
        except:
            company_roleLocation = "NA"

    return companyName, company_starRating, company_offeredRole, company_roleLocation


        
# extracts desired data from listing description
def extract_listingDesc(listing_soup):
    extract_listingDesc_tmpList = []
    listing_jobDesc_raw = None

    try:
        listing_jobDesc_raw = listing_soup.find("div", id="JobDescriptionContainer")
        if type(listing_jobDesc_raw) != type(None):
            JobDescriptionContainer_found = True
        else:
            JobDescriptionContainer_found = False
            listing_jobDesc = "NA"
    except Exception as e:
        print("[ERROR] {} in extract_listingDesc".format(e))
        JobDescriptionContainer_found = False
        listing_jobDesc = "NA"

    if JobDescriptionContainer_found:
        jobDesc_items = listing_jobDesc_raw.findAll('li')
        for jobDesc_item in jobDesc_items:
            extract_listingDesc_tmpList.append(jobDesc_item.text)

        listing_jobDesc = " ".join(extract_listingDesc_tmpList)

        if len(listing_jobDesc) <= 10:
            listing_jobDesc = listing_jobDesc_raw.getText()

    return listing_jobDesc



# extract data from listing
def extract_listing(url):
    request_success = False
    selenium_success = False
    
    #listing_soup, requested_url = requestAndParse(url)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=path, options=options)
    
    try:
        listing_soup, requested_url = requestAndParse(url)
        request_success = True
    except Exception as e:
        print("[ERROR] Error occurred in extract_listing, requested url: {} is unavailable.".format(url))
        return ("NA", "NA", "NA", "NA", "NA", "NA")
    
    # use selenium to scrape company information
    try:
        driver.get(requested_url)
        company_buttom = driver.find_element_by_xpath('//div[@data-tab-type="overview"]')
        company_buttom.click()
        selenium_success = True
        
    except Exception as e:
        print("[ERROR] Error occurred in company information extracting, requested url: {} is unavailable.".format(url))
        year_founded = 'NA'
        company_size = 'NA'
        company_industry = 'NA'
        company_type = 'NA'
        company_sector = 'NA'
        company_revenue = 'NA'
        
    if selenium_success:
        #get year_founded
        try:
            year_founded = driver.find_element_by_id('yearFounded').text
        except:
            year_founded = 'NA'
        
        #get company size
        try:
            company_size = driver.find_element_by_id('size').text
        except:
            company_size = 'NA'
        
        #get industry
        try:
            company_industry = driver.find_element_by_id('primaryIndustry.industryName').text
        except:
            company_industry = 'NA'
        
        #get company_type
        try:
            company_type = driver.find_element_by_id('type').text
        except:
            company_type = 'NA'
        
        #get company_sector
        try:
            company_sector = driver.find_element_by_id('primaryIndustry.sectorName').text
        except:
            company_sector = 'NA'
        
        #get company_revenue
        try:
            company_revenue = driver.find_element_by_id('revenue').text
        except:
            company_revenue = 'NA'
        
        driver.quit()
    if request_success:
        companyName, company_starRating,company_offeredRole, company_roleLocation = extract_listingBanner(listing_soup)
        listing_jobDesc = extract_listingDesc(listing_soup)

    return (companyName, company_starRating,company_offeredRole, company_roleLocation, listing_jobDesc, requested_url, year_founded, company_size, company_industry, company_type, company_sector, company_revenue)
