# Major Prevalance Across States
#### Authors: Rucha Dave, Jiayuan Liu, Emma Mascillaro

## **Project Summary**:
This repository contains our 2022 Software Design Midterm project that web scraps Niche.com to gather data on the prevalance of different majors at the undergraduate level across the US. In order to collect the data, requests were made for the majors and students at the top 10% of colleges in each state as ranked by Niche. In order to understand the prevalance of majors, three separate comparisons were made. The first was the percentage of students at top colleges across America who choose each major. This allowed us to understand what majors were more and less common across the country in general. The second was the the ratio of students from each state who chose each major. This allowed us to understand the most common majors in each state. Finally, we visualized the prevalance of each of the top majors in America across the different states to see if there were any differences.

## **Instructions:**
***Disclaimer**: The website we scraped the data from, Niche.com, has limits for how often and how much data can be scraped. In order to collect the data currently present in raw_data, we stopped running the scraping file everytime we ran into the block and either waited until access was granted again or used another network. Because of this, the current scraping file has the complete list of states commented out and instead, a list has been included with just 2 states. It will create a new folder in the web_scraping folder called testing, where it will store the raw_data.*

*In accordance, we have provided two sets of instructions: one to clean and visualize this shorter set of data which can easily be scraped and another to clean and visualize the data already provided in raw_data, which will match our results. However, we suggest simply running runner_scraper.py to gain an understanding of how we did the web scraping and then using our entire dataset, present in raw_data, to visualize. This can be done by following the second option for our data cleaning and visualization sections*
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

### **Cleaning Data:**
All functions needed to clean the data files are included in the file *data_cleaning.py*. 

Option 1. To clean the data just collected, navigate back to the *web_scraping* folder by running `cd ..` twice. Here, open *data_cleaning.py* and uncomment line 475. This will navigate to the *testing* directory. Then, comment line 477, which remove previously created files. Uncomment line 485 to create a folder called *cleaned_data* in the *testing* directory and comment lines 487 - 489, which also remove previous files. Uncomment lines 473 to 493. Now, running *data_cleaning.py* in the terminal will create a folder called *cleaned_data* within the *testing* directory that contains all the cleaned files.

Option 2. To clean the complete set of data, navigate back to the web_scraping folder by running `cd ..` twice. Here, run *data_cleaning.py*. This will delete the cleaned csvs in *cleaned_data* that currently exist and replace them with the recleaned versions of the files in *raw_data*. Uncomment lines 473 to 493. 

### **Visualizing Data:**
All functions needed to visualize the data files are included in the file *data_visualization.py*.

*Disclaimer: To plot with geopandas, values for all states need to be added, which is not possible when using the self-generated data that is present in the testing file. For this reason, only the first 3 graphs will be seen if plotting with the shorter data. However, using the full raw_data as explained in option 2 will generate all of the plots.*

#### **Setting Up:**
1. Open the GitHub link listed above
2. From here, download the 3 files listed above and move them to the *testing* folder. Inside this folder, move them to the *cleaned_data* folder.

#### **Visualizing:**
Option 1. To visualize the cleaned data for the shorter set that was scraped just now, navigate back to the *web_scraping* directory. Open the file called *data_visualization.py* and uncomment line 15 to navigate to the *testing* folder. Comment out lines 64, 65, 219, 220, 338, and 339. Finally, add `"""` to lines 202 and 333 to comment out the functions that create the US-map graphs, because they cannot be made with data from simply 2 states, as explained above. Then run the file.

Option 2. To visualize our complete set of data, simply navigate back to the *web_scraping* directory and run *data_visualization.py*.
