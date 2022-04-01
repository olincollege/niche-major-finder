"""
This file contains the functions needed to sort through the generated
dataframes, extract necessary information, and create visualizations of the
data to expose trends
"""

import os
import geopandas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV data into Pandas Dataframes
# os.chdir("testing")
os.chdir('cleaned_data')
BROADER_MAJOR_SUMMED_DATA_DF = pd.read_csv("broader_major_summed_data.csv",
                                           header=0)
BROADER_MAJOR_WHOLE_COUNTRY_DF = pd.read_csv(
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
BROADER_MAJOR_WHOLE_COUNTRY_DF['Students'] = BROADER_MAJOR_WHOLE_COUNTRY_DF['Students'].astype(
    int)
BROADER_MAJOR_WHOLE_COUNTRY_DF.sort_values(by=['Students'], inplace=True,
                                           ascending=False)

MAJORS_BY_DESCENDING_POPULARITY = list(BROADER_MAJOR_WHOLE_COUNTRY_DF["Major"])


def total_students_per_state(broader_major_summed_data_frame):
    """
    This function takes a dataframe containing the number of students in all
    majors in all states and returns a list containing the number of students
    in each state.

    Args:
        broader_major_summed_data_frame: A pandas dataframe containing the
        number of students in all majors, in all states.

    Returns:
        all_states_students: A list containing the number of students in each
        state.

    """
    all_states = list(broader_major_summed_data_frame['State'].unique())
    all_states.remove("alaska")
    all_states.remove("hawaii")

    all_states_students = []
    for state in all_states:
        df_this_state = broader_major_summed_data_frame.loc \
            [broader_major_summed_data_frame["State"] == state]
        summed = df_this_state['Students'].sum()
        all_states_students.append(summed)

    return all_states_students



def students_in_a_major_per_state(major):
    """
    Creates a list of the numbers of students enrolled in a major for all states

    Args:
        major:  A string representing the major of interest

    """

    y_current = []

    inner_states_list = list(BROADER_MAJOR_SUMMED_DATA_DF['State'].unique())
    current_major_states_list = list(BROADER_MAJOR_SUMMED_DATA_DF.loc
                                     [BROADER_MAJOR_SUMMED_DATA_DF['Major'] == major, 'State'])

    current_state_index = 0

    while current_state_index < len(inner_states_list):
        if current_major_states_list.count(inner_states_list[current_state_index]) == 0:
            inner_states_list[current_state_index] = 0
            current_state_index += 1
        else:
            current_state_index += 1

    for state in inner_states_list:
        if state != 0:
            y_current.append(int(BROADER_MAJOR_SUMMED_DATA_DF.loc[
                (BROADER_MAJOR_SUMMED_DATA_DF['Major'] == major) &
                (BROADER_MAJOR_SUMMED_DATA_DF['State'] == state),
                'Students']))
        else:
            y_current.append(0)

    return y_current

# Create a list of lists which contain the number of students in each state
# that are majoring in a given major for all majors
i = 0

STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS = []

while i < len(MAJORS_BY_DESCENDING_POPULARITY):
    STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS.append(
        students_in_a_major_per_state(MAJORS_BY_DESCENDING_POPULARITY[i]))

    i += 1

def plot_number_of_students_per_major_usa():
    """
    Create a Bar Chart of the Number of Students in the USA in Each Major

    """

    plt.barh(MAJORS_LIST, STUDENTS_LIST, align="center", alpha=.5)
    plt.title('Number of Students Enrolled in Different Majors Offered by the top 10% of Colleges in Each State')
    plt.xlabel('College Major')
    plt.ylabel('Number of Students Enrolled')
    plt.show()
    plt.savefig("number_of_students_per_major_usa.png")


def plot_major_ratios_in_stacked_bar_graph():
    """
    This function plots the number of students in each of the top 10 US majors
    for each state in a stacked bar graph

    """

    # Convert lists of the number of students studying a major across all
    # states into numpy arrays
    y_1 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[0])
    y_2 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[1])
    y_3 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[2])
    y_4 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[3])
    y_5 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[4])
    y_6 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[5])
    y_7 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[6])
    y_8 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[7])
    y_9 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[8])
    y_10 = np.array(STUDENTS_IN_A_MAJOR_PER_STATE_ALL_MAJORS[9])

    # plot bars in stack manner
    STATES_LIST = list(BROADER_MAJOR_SUMMED_DATA_DF['State'].unique())
    plt.barh(STATES_LIST, y_1, color='r')
    plt.barh(STATES_LIST, y_2, left=y_1)
    plt.barh(STATES_LIST, y_3, left=y_1+y_2)
    plt.barh(STATES_LIST, y_4, left=y_1+y_2+y_3)
    plt.barh(STATES_LIST, y_5, left=y_1+y_2+y_3+y_4)
    plt.barh(STATES_LIST, y_6, left=y_1+y_2+y_3+y_4+y_5)
    plt.barh(STATES_LIST, y_7, left=y_1+y_2+y_3+y_4+y_5+y_6)
    plt.barh(STATES_LIST, y_8, left=y_1+y_2+y_3+y_4+y_5+y_6+y_7)
    plt.barh(STATES_LIST, y_9, left=y_1+y_2+y_3+y_4+y_5+y_6+y_7+y_8)
    plt.barh(STATES_LIST, y_10, left=y_1+y_2+y_3+y_4+y_5+y_6+y_7+y_8+y_9)

    plt.xlabel("Number of Students Enrolled")
    plt.ylabel("State")

    plt.legend([MAJORS_BY_DESCENDING_POPULARITY[0],
                MAJORS_BY_DESCENDING_POPULARITY[1], MAJORS_BY_DESCENDING_POPULARITY[2],
                MAJORS_BY_DESCENDING_POPULARITY[3], MAJORS_BY_DESCENDING_POPULARITY[4],
                MAJORS_BY_DESCENDING_POPULARITY[5], MAJORS_BY_DESCENDING_POPULARITY[6],
                MAJORS_BY_DESCENDING_POPULARITY[7], MAJORS_BY_DESCENDING_POPULARITY[8],
                MAJORS_BY_DESCENDING_POPULARITY[9], MAJORS_BY_DESCENDING_POPULARITY[10]])

    plt.title("Distribution of the Top 10 College Majors in the Country by \
        State")
    plt.show()
    plt.savefig('major_ratios_in_stacked_bar_graph.png')


def plot_major_distribution_in_usa_pie_chart():
    """
    This function plots the percentage of students in each college major across
    the US in a pie chart.

    """
    number_of_students_per_major_usa = np.array(BROADER_MAJOR_WHOLE_COUNTRY_DF \
        ["Students"])
    BROADER_MAJOR_WHOLE_COUNTRY_DF["Students"].to_list()
    plt.pie(number_of_students_per_major_usa,
            labels=BROADER_MAJOR_WHOLE_COUNTRY_DF["Major"].to_list(), rotatelabels=True)
    plt.show()
    plt.savefig("major_distribution_in_usa_pie_chart.png")



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

def generate_business_density_map(BROADER_MAJOR_SUMMED_DATA_DF, RM_STATES_LIST, STATES):

    # Create a list of the number of students majoring in Business in each state
    BUSINESS_MAJORS_BY_STATE = []
    BUSINESS_MAJOR_STATES_LIST = list(BROADER_MAJOR_SUMMED_DATA_DF.loc \
        [BROADER_MAJOR_SUMMED_DATA_DF['Major'] == 'Business', 'State'])

        
    # Reassign a state's name to 0 if there are no business majors in the top 10%
    # of schools in the state
    i = 0

    while i < len(RM_STATES_LIST):
        if BUSINESS_MAJOR_STATES_LIST.count(RM_STATES_LIST[i]) == 0:
            RM_STATES_LIST[i] = 0
            i += 1
        else:
            i += 1


    # Reassign state names with the number of students majoring in business in the
    # respective state
    for current_state in RM_STATES_LIST:
        if current_state != 0:
            BUSINESS_MAJORS_BY_STATE.append(int(BROADER_MAJOR_SUMMED_DATA_DF.loc \
                [(BROADER_MAJOR_SUMMED_DATA_DF['Major'] == "Business") & \
                    (BROADER_MAJOR_SUMMED_DATA_DF['State'] == current_state), \
                        'Students']))
        else:
            BUSINESS_MAJORS_BY_STATE.append(0)

    # Convert the number of students majoring in business per state to a ratio
    # (business majors/all majors)
    BUSINESS_MAJORS_BY_STATE_PERCENT = [i / j for i, j in zip \
        (BUSINESS_MAJORS_BY_STATE, ALL_STUDENTS_PER_STATE)]

    # Add a column to the dataframe containing business major ratio data
    STATES = STATES.assign(Business_Majors=BUSINESS_MAJORS_BY_STATE_PERCENT)

    # Set the coordinate reference system for the STATES shapefile
    STATES.crs = "EPSG:3395"

    # Plot and Save USA Map & Generate scale
    FIG, AX = plt.subplots(1, 1)
    STATES.plot(column='Business_Majors', ax=AX, legend=True)
    plt.show()
    plt.savefig("business_density_map.png")

def generate_engineering_density_map(BROADER_MAJOR_SUMMED_DATA_DF, RM_STATES_LIST, STATES):

    # Create a list of the number of students majoring in Engineering in each state
    ENGINEERING_MAJORS_BY_STATE = []
    ENGINEERING_MAJOR_STATES_LIST = list(BROADER_MAJOR_SUMMED_DATA_DF.loc \
        [BROADER_MAJOR_SUMMED_DATA_DF['Major'] == 'Engineering', 'State'])

    # Reassign a state's name to 0 if there are no engineering majors in the
    # top 10% of schools in the state
    i = 0

    while i < len(RM_STATES_LIST):
        if ENGINEERING_MAJOR_STATES_LIST.count(RM_STATES_LIST[i]) == 0:
            RM_STATES_LIST[i] = 0
            i += 1
        else:
            i += 1

    # Reassign state names with the number of students majoring in engineering
    # in the respective state
    for current_state in RM_STATES_LIST:
        if current_state != 0:
            ENGINEERING_MAJORS_BY_STATE.append(int\
                (BROADER_MAJOR_SUMMED_DATA_DF.loc[(BROADER_MAJOR_SUMMED_DATA_DF \
                    ['Major'] == "Engineering") & (BROADER_MAJOR_SUMMED_DATA_DF \
                        ['State'] == current_state), 'Students']))
        else:
            ENGINEERING_MAJORS_BY_STATE.append(0)

    # Convert the number of students majoring in engineering per state to a ratio
    # (business majors/all majors)
    ENGINEERING_MAJORS_BY_STATE_PERCENT = [i / j for i, j in zip \
        (ENGINEERING_MAJORS_BY_STATE, ALL_STUDENTS_PER_STATE)]

    # Add a column to the dataframe containing engineering major ratio data
    STATES = STATES.assign(Engineering_Majors=ENGINEERING_MAJORS_BY_STATE_PERCENT)

    # Set the coordinate reference system for the STATES shapefile
    STATES.crs = "EPSG:3395"

    # Plot and Save USA Map & Generate scale
    FIG, AX = plt.subplots(1, 1)
    STATES.plot(column='Engineering_Majors', ax=AX, legend=True)
    plt.show()
    plt.savefig("engineering_density_map.png")
