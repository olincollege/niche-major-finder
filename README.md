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
All functions needed to scrap Niche are included in the file *niche_web_scraping.py*. 

In order to run this, run the following command in the terminal to navigate to the web_scraping folder: `cd web_scraping`. Run the *runner_scraping.py* file. This will create a folder called *testing* within the web_scraping folder which will contain a folder called *raw_data*, which will have csv files for all the data scraped. 

In order to run the full list of states and obtain all the data, comment line 133 in *niche_web_scraping.py* and uncomment lines 122-131. This will loop through all the states. Because of the timeout errors due to Niche.com's rules, change the states_list variable to include only the states that haven't been scraped yet every time the error occurs. Then, comment out lines 14 and 18 in the *runner_scraping.py* file to stop from remaking the folders. Rerun *runner_scraping.py* once scraping can be resumed.

### **Cleaning and Visualizing Data:**
All functions needed to clean the data files are included in the file *data_cleaning.py* and functions needed to visualize the data are included in the file *data_visualization.py*. 

To clean the data just collected, navigate back to the *web_scraping* folder by running `cd ..` twice. Here, open *runner.py* and uncomment line 19. This will navigate to the *testing* directory. Then, comment lines 20 and 21, which remove previously created files. Uncomment line 29 to create a folder called *cleaned_data* in the *testing* directory

To clean the complete set of data and run the visualization we did for our project, navigate back to the web_scraping folder by running `cd ..` twice. Here, run *runner.py*. This will delete the csvs in *cleaned_data* that include cleaned versions of the data. 






