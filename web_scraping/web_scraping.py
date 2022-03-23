import requests
from bs4 import BeautifulSoup as BS

agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

# Access each college website
college_url = f"http://webcache.googleusercontent.com/search?q=cache:https://www.niche.com/colleges/university-of-alabama---birmingham/"
college_page = requests.get(college_url, headers=agent)
college_html = BS(college_page.text, "html.parser")

# Loop through information for each major on the website and add to df
top_majors = college_html.select("div.popular-entity")

for major in top_majors:
    if major.select(".popular-entity-descriptor"):
        print(major.select('.popular-entity__name')[0].get_text())
        print(major.select('.popular-entity-descriptor')[0].get_text())
        print("Alabama")
        print("auburn-university")