"""
This file runs all cleaning and visualization processes for the data gathered
through web scraping. In order to run this on the full raw_data folder, the
file can be run as it is. Else, navigate to the folder containing the data
to be cleaned and visualized.
"""

import os

import data_cleaning as dc
import data_visualization as dv
import pandas as pd


# Remove previous attempts
os.system("cd raw_data")
os.system("rm combined_data.csv")

# Combine data files for all states in folder and read to Pandas DataFrame
dc.files_to_df()
df = pd.read_csv("combined_data.csv")

# Remove previous attempts
os.system("cd ..")
os.system("cd cleaned_data")
os.system("rm broader_major_combined_data.csv")
os.system("rm broader_major_summed_data.csv")
os.system("rm broader_major_whole_country.csv")

# Create cleaned csv files
dc.create_csvs(df)


# Read CSV data into Pandas Dataframes
os.system("cd cleaned_data")

BROADER_MAJOR_SUMMED_DATA_DF = pd.read_csv("broader_major_summed_data.csv", \
    header=0)
BROADER_MAJOR_WHOLE_COUNTRY_DF = pd.read_csv( \
    'broader_major_whole_country.csv', names=["Major", "Students"], header=0)

# Input # of students in the USA per major data into integer lists
MAJOR = BROADER_MAJOR_WHOLE_COUNTRY_DF["Major"]
STUDENTS = BROADER_MAJOR_WHOLE_COUNTRY_DF["Students"]

MAJORS_LIST = list(MAJOR[:])
STUDENTS_LIST = list(STUDENTS[:])

STUDENT_LIST_INDEX = 0

while STUDENT_LIST_INDEX < len(STUDENTS_LIST):
    STUDENTS_LIST[STUDENT_LIST_INDEX] = int(STUDENTS_LIST[STUDENT_LIST_INDEX])

    STUDENT_LIST_INDEX += 1

# Create a List of All State Names
STATES_LIST = list(BROADER_MAJOR_SUMMED_DATA_DF['State'].unique())

# Order Majors by Popularity in the USA
BROADER_MAJOR_WHOLE_COUNTRY_DF['Students'] = BROADER_MAJOR_WHOLE_COUNTRY_DF \
    ['Students'].astype(int)
BROADER_MAJOR_WHOLE_COUNTRY_DF.sort_values(by=['Students'], inplace=True, \
    ascending=False)

MAJORS_BY_DESCENDING_POPULARITY = list(BROADER_MAJOR_WHOLE_COUNTRY_DF["Major"])

# Create a list of lists which contain the number of students in each state
# that are majoring in a given major for all majors
i = 0

STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS = []

while i < len(MAJORS_BY_DESCENDING_POPULARITY):
    STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS.append \
        (dv.students_in_a_major_per_state(MAJORS_BY_DESCENDING_POPULARITY[i]))

    i += 1

ALL_STUDENTS_PER_STATE = total_students_per_state(BROADER_MAJOR_SUMMED_DATA_DF)

# Read shape file to create a bas USA map
STATES = geopandas.read_file("usa-states-census-2014.shp")

# Sort the dataframe alphabetically by state names
STATES.sort_values("NAME", axis=0, ascending=True, inplace=True, \
    na_position="last")

# Remove repeated states and Washington DC
STATES = STATES.drop(labels=[1, 49, 50, 51, 52, 53, 54, 55, 56, 57], axis=0)

# Remove Alaska & Hawaii from the state list
# (map shape file only has continental states)
RM_STATES_LIST = STATES_LIST
RM_STATES_LIST.remove("alaska")
RM_STATES_LIST.remove("hawaii")

dv.plot_number_of_students_per_major_usa()
dv.plot_major_ratios_in_stacked_bar_graph()
dv.plot_major_distribution_in_usa_pie_chart()
dv.generate_business_density_map(BROADER_MAJOR_SUMMED_DATA_DF, RM_STATES_LIST, STATES)
dv.generate_engineering_density_map(BROADER_MAJOR_SUMMED_DATA_DF, RM_STATES_LIST, STATES)
