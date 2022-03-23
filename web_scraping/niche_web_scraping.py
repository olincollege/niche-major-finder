import requests
import math
import pandas as pd

from bs4 import BeautifulSoup as BS

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# Create pandas dataframe
df = pd.DataFrame()

states_list = ["alabama"]

for i in states_list:
    # Find text from the college listings for each state
    url = f"https://www.niche.com/colleges/search/all-colleges/s/{i}/?type=private&type=communityCollege&type=public"
    page = requests.get(url, headers=agent)
    html = BS(page.text, "html.parser")
    print(html)
    # Get the total number of colleges in the state from the text
    #number_of_colleges = html.select('.search-result-counter')[0].get_text()
    #number_of_colleges = int(number_of_colleges[:-8])

    # Find the number of colleges in the top 10% for each state
    #top_ten_percent_of_colleges = math.ceil(0.1 * number_of_colleges)
    top_ten_percent_of_colleges = 10

    # Loop through all colleges on first page while total < 10% number
    colleges = html.find_all(attrs={'class':"search-result"})
    total_colleges_yet = 0

    while total_colleges_yet < top_ten_percent_of_colleges:
        college = colleges[total_colleges_yet]
        college_name = college["aria-label"].replace(" ", "-")

        # Access each college website
        college_url = f"https://www.niche.com/colleges/{college_name}/"
        college_page = requests.get(college_url, headers=agent)
        college_html = BS(college_page.text, "html.parser")

        # Loop through information for each major on the website and add to df
        top_majors = college_html.find_all(attrs={'class':"popular-entity"})

        for major in top_majors:
            df["Major"] = major.select('.popular-entity__name')[0].get_text()
            df["Students"] = major.select('.popular-entity-descriptor')[0].get_text()
            df["State"] = i
            df["Name"] = college["aria-label"]

        total_colleges_yet += 1
    print(df)