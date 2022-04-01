# Major Prevalance Across States
#### Authors: Rucha Dave, Jiayuan Liu, Emma Mascillaro

## **Project Summary**:
This repository contains our 2022 Software Design Midterm project that web scraps Niche.com to gather data on the prevalance of different majors at the undergraduate level across the US. In order to collect the data, requests were made for the majors and students at the top 10% of colleges in each state as ranked by Niche. In order to understand the prevalance of majors, three separate comparisons were made. The first was the percentage of students at top colleges across America who choose each major. This allowed us to understand what majors were more and less common across the country in general. The second was the the ratio of students from each state who chose each major. This allowed us to understand the most common majors in each state. Finally, we visualized the prevalance of each of the top majors in America across the different states to see if there were any differences.

## **Instructions:**
***Disclaimer**: The website we scraped the data from, Niche.com, has limits for how often and how much data can be scraped. In order to collect the data currently present in raw_data, we stopped running the scraping file everytime we ran into the block and either waited until access was granted again or used another network. Because of this, the current scraping file has the complete list of states commented out and instead, a list has been included with just 2 states. It will create a new folder in the web_scraping folder called testing, where it will store the raw_data. In accordance, two sets of instructions have been provided: one to clean and visualize this shorter set of data which can easily be scraped and another to clean and visualize the data already provided in raw_data, which will match our results.*
### **Dependancies:**

In order to collect, clean, and visualize the our data, we utiziled mutliple Python libraries. 

Data Scraping:
1. os - This should come as part of the Python package
2. math - This should come as part of the Python package
3. time - This should come as part of the Python package
4. requests - `pip install requests`
5. pandas - `pip install pandas`
6. BeautifulSoup - `pip install beautifulsoup4`

Data Cleaning:
1. glob - This should come as part of the Python package

Data Visualizing: 
1. geopandas - `pip install geopandas`
2. numpy - `pip install numpy`
3. matplotlib - `pip install matplotlib`

### **Running Scraping:**








