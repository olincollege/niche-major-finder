import niche_web_scraping as nws
import os

"""
Running this file will create a folder called testing in the directory
with a shorter version of the raw_data collected through web scraping. The
purpose of this is to ensure that the web scraping functions work without
running into an error because the code timed out or without altering the
current data that has already been collected.
"""

# Used to ensure actual data isn't altered while testing the driver. Remove 
# this if trying to copy our process.
os.mkdir('testing') 
os.chdir('testing')

# Create folder for scraped data
os.mkdir('raw_data')
os.chdir('raw_data')

# Scrape data for top 10% of colleges in each state in the list
nws.run_scraping()