import requests
import math
import pandas as pd
import time

from bs4 import BeautifulSoup as BS

agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

# Create data list
data = []
#states_list = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]

#for i in states_list:
    # Find text from the college listings for each state
url = f"https://www.niche.com/colleges/search/all-colleges/s/arizona/?type=private&type=communityCollege&type=public"
page = requests.get(url, headers=agent)
html = BS(page.text, "html.parser")
print(html)

    # Get the total number of colleges in the state from the text
number_of_colleges = html.select('.search-result-counter')[0].get_text()
number_of_colleges = int(number_of_colleges[:-8])

    # Find the number of colleges in the top 10% for each state
top_ten_percent_of_colleges = math.ceil(0.1 * number_of_colleges)

    # Loop through all colleges on first page while total < 10% number
colleges = html.find_all(attrs={'class':"search-result"})
total_colleges_yet = 0

while total_colleges_yet < top_ten_percent_of_colleges:
    college = colleges[total_colleges_yet]
    college_name = college["aria-label"]
    college_name = college_name.lower()
    college_name = college_name.replace(" ", "-")

        # Access each college website
    college_url = f"https://www.niche.com/colleges/{college_name}/"
    college_page = requests.get(college_url, headers=agent)
    college_html = BS(college_page.text, "html.parser")

        # Loop through information for each major on the website and add to df
    top_majors = college_html.select("div.popular-entity")

    for major in top_majors:
            # Filter out results that aren't actually majors
        if major.select(".popular-entity-descriptor"):
            major_name = major.select('.popular-entity__name')[0].get_text()
            major_students = major.select('.popular-entity-descriptor')[0].get_text()
            major_students = int(major_students[:-10])
            data.append([i, college_name, major_name, major_students])

    total_colleges_yet += 1
    time.sleep(5)
print(data)

import pandas as pd
import os
import glob

def files_to_df():
    """
    This function __FINISH__
    Args:
        folder_name:

    Returns:

    """
    os.chdir("raw_data")
    all_filenames = sorted([i for i in glob.glob("*.{}".format("csv"))])
    print(all_filenames)
    print([pd.read_csv(f) for f in all_filenames])

files_to_df()