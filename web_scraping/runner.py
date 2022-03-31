"""
This file runs all cleaning and visualization processes for the data gathered
through web scraping. In order to run this on the full raw_data folder, the
file can be run as it is. Else, navigate to the folder containing the data
to be cleaned and visualized.
"""

import os
import pandas as pd

import data_cleaning as dc
#import data_visualization as dv

# Remove previous attempts
os.chdir("raw_data")
os.remove("combined_data.csv")

# Combine data files for all states in folder and read to Pandas DataFrame
dc.files_to_df()
df = pd.read_csv("combined_data.csv")

# Remove previous attempts
os.chdir("..")
os.chdir("cleaned_data")
os.remove("broader_major_combined_data.csv")
os.remove("broader_major_summed_data.csv")
os.remove("broader_major_whole_country.csv")

# Create cleaned csv files
dc.create_csvs(df)

#
