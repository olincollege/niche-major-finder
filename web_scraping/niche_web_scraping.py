import requests
import math
import pandas as pd
import time

from bs4 import BeautifulSoup as BS


# Create data list
states_list = ["alabama", "alaska"]
#, "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]

for i in states_list:
    data = []
    # Find text from the college listings for each state
    url = f"https://www.niche.com/colleges/search/all-colleges/s/{i}/?type=private&type=communityCollege&type=public"
    page = requests.get(url)
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
        college_url = f"http://webcache.googleusercontent.com/search?q=cache:https://www.niche.com/colleges/{college_name}/"
        college_page = requests.get(college_url)
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
        df = pd.DataFrame(data, columns=["State", "College", "Major", "Students"])
        df.to_csv(f"{i}Data.csv", index=False)
        print(data)
        time.sleep(20)
    
