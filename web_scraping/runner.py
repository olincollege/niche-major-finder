import data_cleaning as dc
import data_visualization as dv

import pandas as pd
import os

os.chdir("raw_data")
os.remove('combined_data.csv')
dc.files_to_df() # --> to create combined_data.csv
df = pd.read_csv("combined_data.csv")
 
os.chdir('..')
os.chdir('cleaned_data')
os.remove('broader_major_combined_data.csv')
os.remove('broader_major_summed_data.csv')
os.remove('broader_major_whole_country.csv')
os.chdir('..')
os.rmdir('cleaned_data')
os.makedirs('cleaned_data')
os.chdir('cleaned_data')

dc.create_csvs(df)