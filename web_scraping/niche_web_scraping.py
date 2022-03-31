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

def get_html_for_url(url, agent):
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

def filter_majors(major, curr_data, state, college_name):
    """
    This function filters out entries that are not the top 10% colleges, and
    focuses on the entries that are colleges and go through them to get the

    Args:
        major: A CSS element that is taken from the list return by the
        select function of beautiful soup function, representing the majors
        in a college.
        curr_data: A list that add state, college name, major name, and student
        in that major for each college.
        state: A string that represents the state of the college.
        college_name: A string that represents the college.

    Return:
        curr_data: A list of lists that contains state, college name, major
        name, and student in that major for different colleges.
    """
    if major.select(".popular-entity-descriptor"):
        major_name = major.select('.popular-entity__name')\
            [0].get_text()
        major_students = major.select('.popular-entity-descriptor')\
            [0].get_text()
        major_students = int(major_students[:major_students.find(' ')\
            ].replace(',', ''))
        curr_data.append([state, college_name, major_name, major_students])

    return curr_data

def find_college_name(college):
    """
    This function finds the college name and modify the name to be in lowercase,
    and all spaces are replaced by "-"

    Arg: 
        college: A string that contains the name of the college.
    
    Return:
        college_name: A string that represents the college name after it is
        being extracted and modified.
    """
    college_name = college["aria-label"]
    college_name = college_name.lower()
    college_name = college_name.replace(" ", "-")
    return college_name


def run_scraping():
    """
    This function goes through the niche website, scraps and stores data of
    state, college, major, number of students in that major in a csv file.

    This function opens niche webpage for each state in the list and loops
    through the top 10% of colleges in each state. In the webpage for each
    college, this function looks for all majors listed and the number of
    students that graduated with those majors. It then records this data in
    lists and stores them into a csv file.

    """
    # Agent for scraping header
    agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKi"
    + "t/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    # When running this file for all states, we would get timeout errors from
    # requests. The data in raw_data was gathered by running the file multiple
    # times through various different VPNs. To make the process simpler, we have
    # commented out the full list and instead included a list of 2 states that
    # should provide enough data for testing purposes

    # states_list = ["alabama", "alaska", "arizona", "arkansas", "california", \
    # "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", \
    # "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana"\
    # , "maine", "maryland", "massachusetts", "michigan", "minnesota", \
    # "mississippi", "missouri", "montana", "nebraska", "nevada", \
    # "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina"\
    # , "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", \
    # "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", \
    # "utah", "vermont", "virginia", "washington", "west-virginia", \
    # "wisconsin", "wyoming"]

    states_list = ["hawaii", "idaho"]

    for state in states_list:
        data = []

        # Find text from the college listings for each state
        html = get_html_for_url("https://www.niche.com/"
        + f"colleges/search/all-colleges/s/{state}/", agent)

        # Get the total number of colleges in the state from the text
        number_of_colleges = html.select('.search-result-counter')[0].get_text()
        number_of_colleges = int(number_of_colleges[:-8].replace(',', ''))

        # Find the number of colleges in the top 10% for each state
        top_ten_percent_of_colleges = math.ceil(0.1 * number_of_colleges)

        # Loop through all colleges while total < 10% of the total number of 
        # colleges in the state

        colleges = html.find_all(attrs={'class':"search-result"})
        total_colleges_yet = 0
        index_on_page = 0
        current_page_number = 1

        while total_colleges_yet < top_ten_percent_of_colleges:
            # Pause for 20 sec to allow scraping
            time.sleep(20)

            college = colleges[index_on_page]
            college_name = find_college_name(college)        

            # Access each college website
            college_html = get_html_for_url\
                (f"https://www.niche.com/colleges/{college_name}/", agent)

            # Loop through information for each major on the website and add to data
            top_majors = college_html.select("div.popular-entity")

            # Filter out results that aren't actually majors
            for major in top_majors:
                data = filter_majors(major, data, state, college_name)

            # Move to next college
            index_on_page += 1

            # Move to next page if needed
            if index_on_page == 25:
                current_page_number += 1
                html = get_html_for_url("https://www.niche.com/"
                    + f"colleges/search/all-colleges/s/{state}/?page=" +
                    f"{current_page_number}", agent)
                colleges = html.find_all(attrs={'class':"search-result"})

                # Reset page index on next page
                index_on_page = 0

            total_colleges_yet += 1

            # Create csv for each state's data
            df = pd.DataFrame(data, columns=["State", "College", "Major", \
                "Students"])
            df.to_csv(f"{state}Data.csv", index=False)
