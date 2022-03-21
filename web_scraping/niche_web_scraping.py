import requests
import math

from bs4 import BeautifulSoup as BS


agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

states = ["alabama"]

for i in states:
    url = f"https://www.niche.com/colleges/search/all-colleges/s/{i}/?type=private&type=communityCollege&type=public"
    page = requests.get(url, headers=agent)
    #print (BS(page.content, 'lxml'))
    html = BS(page.text, "html.parser")
    colleges = html.select("ol.search-results__list")
    #print(colleges)

    # Get the number of colleges in a state from the number of results produced
    number_of_colleges = html.select(".search-result-counter")[0].get_text()
    number_of_colleges = int(number_of_colleges[:-8])

    # Find the number of colleges in the top 10%
    top_ten_percent_of_colleges = math.ceil(0.1 * number_of_colleges)

    # Get the information on the colleges in the top 10%
    # Name, number of ppl per major, total students
    # *Convert to pandas dataframe
    
    for college in colleges:
        college_title = college.select('.search-result__title')[0].get_text()
        print(colleges)
        print(college_title)