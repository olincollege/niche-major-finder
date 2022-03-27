import requests
import math
import pandas as pd
import time

from bs4 import BeautifulSoup as BS

"""
This file 
"""

def get_html_for_url(url):
    page = requests.get(url, headers=agent, timeout=7)
    html = BS(page.text, "html.parser")
    return html

# Agent for scraping header
agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

# Find top 10% of colleges for each state
states_list = ["oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]

for i in states_list:
    data = []

    # Find text from the college listings for each state
    #html = get_html_for_url(f"http://webcache.googleusercontent.com/search?q=cache:https://www.niche.com/colleges/search/all-colleges/s/{i}/?page=2/")
    html = get_html_for_url(f"https://www.niche.com/colleges/search/all-colleges/s/{i}/")

    # Get the total number of colleges in the state from the text
    number_of_colleges = html.select('.search-result-counter')[0].get_text()
    number_of_colleges = int(number_of_colleges[:-8].replace(',', ''))

    # Find the number of colleges in the top 10% for each state
    top_ten_percent_of_colleges = math.ceil(0.1 * number_of_colleges)
    print(top_ten_percent_of_colleges)

    # Loop through all colleges on first page while total < 10% number
    colleges = html.find_all(attrs={'class':"search-result"})
    total_colleges_yet = 0
    index_on_page = 0
    current_page = 1
    
    while total_colleges_yet < top_ten_percent_of_colleges:
        # Pause for 20 sec to allow scraping
        time.sleep(20)

        college = colleges[index_on_page]

        # Find name of college
        college_name = college["aria-label"]
        college_name = college_name.lower()
        college_name = college_name.replace(" ", "-")

        # Access each college website
        college_html = get_html_for_url(f"https://www.niche.com/colleges/{college_name}/")
        #college_html = get_html_for_url(f"http://webcache.googleusercontent.com/search?q=cache:https://www.niche.com/colleges/{college_name}/")
        print(college_html)

        # Loop through information for each major on the website and add to data
        top_majors = college_html.select("div.popular-entity")

        for major in top_majors:

            # Filter out results that aren't actually majors
            if major.select(".popular-entity-descriptor"):
                major_name = major.select('.popular-entity__name')[0].get_text()
                major_students = major.select('.popular-entity-descriptor')[0].get_text()
                major_students = int(major_students[:major_students.find(' ')].replace(',', ''))
                data.append([i, college_name, major_name, major_students])

        # Move to next college
        index_on_page += 1

        # Move to next page if needed
        if index_on_page == 25:
            current_page += 1
            #html = get_html_for_url(f"http://webcache.googleusercontent.com/search?q=cache:https://www.niche.com/colleges/search/all-colleges/s/{i}/?page={current_page}")
            html = get_html_for_url(f"https://www.niche.com/colleges/search/all-colleges/s/{i}/?page={current_page}")
            colleges = html.find_all(attrs={'class':"search-result"})

            # Reset page index
            index_on_page = 0
        total_colleges_yet += 1

        # Create csv for each state's data
        df = pd.DataFrame(data, columns=["State", "College", "Major", "Students"])
        df.to_csv(f"{i}Data.csv", index=False)
        print(data)

        
    
