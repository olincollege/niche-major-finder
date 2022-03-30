"""
This file scraps data from niche.com to get college majors distribution for
each of the top 10% of colleges in every US state.

This file takes in the url of niche.com and go through the pages for every state
in the US. It finds the major distribution data on the page for each of the
top 10% ranked colleges. For each major in each college, the data is stored in
a csv file with four columns for state, college name, major name, and the number
of students who graduated with that major in 2022.

Each .csv file contains data for all or part of the top 10% colleges in one
state. Even with the usage of google cache and agent, this file still can't get
data for all colleges in every state in one run. Therefore, multiple csv files
are created with each run of this file.

"""
import math
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
import os

def get_html_for_url(url):
    """
    This function takes in the url of a webpage that we acquire data from and
    returns a variable that stores all the text displayed on this webpage.
    Args:
        url: The website url that we are acquiring data from.

    Returns:
        All the text displayed on the webpage with the input url.
    """
    page = requests.get(url, headers=agent, timeout=7)
    page_text = BS(page.text, "html.parser")
    return page_text

# Create folder for data scraped
os.mkdir('raw_data')
os.chdir('raw_data')

# Agent for scraping header
agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53"
+"7.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

# Find top 10% of colleges for each state in the state list
states_list = ["alabama"]
# With a single run of this file, the data we get before being blocked by the
# webpage are all in the state of alabama. Therefore, to test if this file works
# please use "alabama" as the only element in the list, in case it takes too
# long or leads to an error.

# states_list = ["alabama", "alaska", "arizona", "arkansas", "california", \
# "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", \
# "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana",\
#  "maine", "maryland", "massachusetts", "michigan", "minnesota", \
# "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire",\
#  "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", \
# "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island",\
#  "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont",\
#  "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]

for state in states_list:
    data = []

    # Find text from the college listings for each state
    html = get_html_for_url("https://www.niche.com/"
    + f"colleges/search/all-colleges/s/{state}/")

    # Get the total number of colleges in the state from the text
    number_of_colleges = html.select('.search-result-counter')[0].get_text()
    number_of_colleges = int(number_of_colleges[:-8].replace(',', ''))

    # Find the number of colleges in the top 10% for each state
    top_ten_percent_of_colleges = math.ceil(0.1 * number_of_colleges)

    # Loop through all colleges while total < 10% of the total number of 
    # colleges in the state

    colleges = html.find_all(attrs={'class':"search-result"})
    TOTAL_COLLEGES_YET = 0
    INDEX_ON_PAGE = 0
    CURRENT_PAGE = 1

    while TOTAL_COLLEGES_YET < top_ten_percent_of_colleges:
        # Pause for 20 sec to allow scraping
        time.sleep(20)

        college = colleges[INDEX_ON_PAGE]

        # Find name of college
        college_name = college["aria-label"]
        college_name = college_name.lower()
        college_name = college_name.replace(" ", "-")

        # Access each college website
        college_html = get_html_for_url\
            (f"https://www.niche.com/colleges/{college_name}/")

        # Loop through information for each major on the website and add to data
        top_majors = college_html.select("div.popular-entity")

        for major in top_majors:

            # Filter out results that aren't actually majors
            if major.select(".popular-entity-descriptor"):
                major_name = major.select('.popular-entity__name')\
                    [0].get_text()
                major_students = major.select('.popular-entity-descriptor')\
                    [0].get_text()
                major_students = int(major_students[:major_students.find(' ')\
                    ].replace(',', ''))
                data.append([state, college_name, major_name, major_students])

        # Move to next college
        INDEX_ON_PAGE += 1

        # Move to next page if needed
        if INDEX_ON_PAGE == 25:
            CURRENT_PAGE += 1
            html = get_html_for_url("https://www.niche.com/"
            +f"colleges/search/all-colleges/s/{state}/?page={CURRENT_PAGE}")
            colleges = html.find_all(attrs={'class':"search-result"})

            # Reset page index on next page
            INDEX_ON_PAGE = 0

        TOTAL_COLLEGES_YET += 1

        # Create csv for each state's data
        df = pd.DataFrame(data, columns=["State", "College", "Major", \
            "Students"])
        df.to_csv(f"{state}Data.csv", index=False)
