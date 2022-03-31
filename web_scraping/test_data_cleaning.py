"""
Test functions in data_cleaning.py are working properly.
"""
import os
import pytest
import pandas as pd

from data_cleaning import (
    get_key,
    find_broader_major
)

TESTING_DICT = {'Computer Science': ['Computer Science',\
    'Computer Software Engineering', 'Information Technology', \
    'Computer Programming', 'Data Processing', \
    'Computer and Information Sciences', 'Human Computer Interaction', \
    'Computer Systems Networking and Telecommunications', \
    'Network, Database, and System Administration', \
    'Computer and Information Systems Security', \
    'Computer Engineering Technician', 'Systems Science and Theory'],
    'Science': ['Physical Sciences', 'Physics', 'Engineering Physics', \
    'Chemistry', 'Apparel and Textile Science', \
    'Pharmacology and Toxicology', 'Bioinformatics', 'Cellular Biology', \
    'Biology', 'Biochemistry and Molecular Biology', \
    'Ecology and Evolutionary Biology', 'Microbiology'],
    'Math': ['Mathematics', 'Computational and Applied Mathematics', \
    'Statistics'],
    'Psychology': ['Psychology', 'Physiological Psychology', \
    'Research and Experimental Psychology', 'Counseling Psychology', \
    'Psychiatric and Mental Health Services', \
    'Developmental and Child Psychology', 'Social Psychology', \
    'Human Development', 'Mental and Social Health Services',\
    'Community Health Services and Counseling',\
    'Marriage and Family Therapy and Counseling', 'Cognitive Science'],
    'Agriculture and Environment': ['Agricultural Engineering', \
    'Agricultural Mechanics and Machinery', \
    'Sustainability Studies', 'Environmental Science', \
    'Wildlife and Fisheries Management', \
    'Natural Resources Conservation and Management', \
    'Zoology and Entomology', 'Marine Science', \
    'Atmospheric Sciences and Meteorology', 'Geology and Earth Science', \
    'Geography', 'Marine Biology and Oceanography', 'Natural Sciences', \
    'Landscaping and Groundskeeping']}

#os.chdir("testing/raw_data")
#data_cleaning.files_to_df()
#hawaii_and_idaho = pd.read_csv("combined_data.csv")


# Define sets of test cases
get_key_cases = [
    # Check that value in the dictionary returns the right category
    (['Agricultural Engineering', \
    'Agricultural Mechanics and Machinery', \
    'Sustainability Studies', 'Environmental Science', \
    'Wildlife and Fisheries Management', \
    'Natural Resources Conservation and Management', \
    'Zoology and Entomology', 'Marine Science', \
    'Atmospheric Sciences and Meteorology', 'Geology and Earth Science', \
    'Geography', 'Marine Biology and Oceanography', 'Natural Sciences', \
    'Landscaping and Groundskeeping'],\
    TESTING_DICT, "Agriculture and Environment"),
    # Check that value not in dictionary returns None
    ("Assignment", TESTING_DICT, None),
    # Check that empty string returns None
    ("", TESTING_DICT, None)
]

find_broader_major_cases = [
    # Check that a specific major in broader_dict returns the correct broader
    # major
    ("Marine Science", "Agriculture and Environment"),
    ("Apparel and Textile Science", "Science"),
    # Check that a broader major entered returns None
    ("Humanities", None),
    # Check that a string not in the dictionary as a value or key returns None
    ("aer", None),
    # Check that an empty string returns None
    ("", None)
]

sum_broad_major_per_state_cases = [
    # Check that a certain state has been summed correctly
    ("hawaii", "Humanities", 240),
    ("idaho", "Engineering", 182)
]

sum_broad_major_per_state_no_repeats_cases = [
    # Check that the summed df (csv created through the df) has no repeat majors
    # for the state. This ensures that all similar values have been summed
    ("arizona"),
    ("pennsylvania")
]

sum_broad_major_country_cases = [
    # Check that the summed csv for all states has been summed correctly
    ("History and World Studies", 2924),
    ("Math", 5949)
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.

def test_files_to_df_first_row():
    """
    Check that the concatenation of files for all files in raw_data has worked
    by checking the first row of the csv. Need to navigate into folder.
    """
    os.chdir('raw_data')
    dataframe = pd.read_csv('combined_data.csv', header=[0])
    assert (dataframe.iloc[0].values.tolist() == \
        ['alabama','auburn-university', \
        'Biomedical Sciences and Molecular Medicine', 305])

def test_files_to_df_last_row():
    """
    Check that the concatenation of files for all files in raw_data has worked
    by checking the first row of the csv. Need to navigate into folder.
    """
    dataframe = pd.read_csv('combined_data.csv', header=[0])
    assert (dataframe.iloc[-1].values.tolist() == \
        ['wyoming','university-of-wyoming','Business', 63])

@pytest.mark.parametrize("value_entered, dict, key_name", get_key_cases)
def test_get_key(value_entered, dictionary, key_name):
    """
    Check that get_key returns the key that corresponds to the input value.

    Args:
        value_entered: A list that is one of the value in a dictionary
        dictionary: A dictionary mapping strings to lists.
        key_name: A string representing the key for the value entered in the
            dictionary that is expected to be returned.+
    """
    assert get_key(value_entered, dictionary) == key_name

@pytest.mark.parametrize("specific_major, broader_major", \
    find_broader_major_cases)
def test_find_broader_major(specific_major, broader_major):
    """
    Check that find_broader_major returns the broader major for the major name
    when entered.

    Args:
        specific_major: A string representing the specific major name.
        broader_major: A string representing the broader major name expected to
            be returned.

    """
    assert find_broader_major(specific_major) == broader_major

def test_replace_major_with_broader_major():
    """
    Check that the csv created by running this function contains replaced
    major names.
    """
    os.chdir('..')
    os.chdir('cleaned_data')

    dataframe = pd.read_csv('broader_major_combined_data.csv', header=[0])
    assert dataframe.iloc[0][2] == 'Health Science'

def test_replace_major_with_broader_major_invalid():
    """
    Check that the csv created by running this function doesn't contain any
    specific major names.
    """
    dataframe = pd.read_csv('broader_major_combined_data.csv', header=[0])
    assert ("Mechanical Engineering" in dataframe["Major"].values) is False

def test_replace_major_with_broader_major_non_empty():
    """
    Check that there are no rows with empty strings for major names
    """
    dataframe = pd.read_csv('broader_major_combined_data.csv', header=[0])
    assert dataframe["Major"].isnull().values.any() is False

@pytest.mark.parametrize("state_name, major_name, total_students", \
    sum_broad_major_per_state_cases)
def test_sum_broad_major_per_state(state_name, major_name, total_students):
    """
    Check that the csv created by running this function has correctly summed
    all students in a certain state who majored in a certain group.

    Args:
        state_name: A string consisting of the name of the state for which the
            test is being run.
        major_name: A string consisting of the name of the major for which the
            test is being run.
        total_students: An integer represeting the expected result for the total
            number of students in the state majoring in the entered major
    """
    dataframe = pd.read_csv('broader_major_summed_data.csv', header=[0])
    df_this_state = dataframe.loc[dataframe["State"] == state_name]

    df_this_state_this_major = df_this_state.loc\
        [dataframe["Major"] == major_name]
    assert df_this_state_this_major.iloc[0][2] == total_students

@pytest.mark.parametrize("state_name", \
    sum_broad_major_per_state_no_repeats_cases)
def test_sum_broad_major_per_state_no_repeats(state_name):
    """
    Check that there are no repeats in the majors list for each state by
    comparing the total unique values to the total values for the state

    Args:
        state_name: A string representing the name of the state to be checked
    """
    dataframe = pd.read_csv('broader_major_summed_data.csv', header=[0])
    df_this_state = dataframe.loc[dataframe["State"] == state_name]

    total_values = len(df_this_state)
    unique_values = len(df_this_state["Major"].unique())

    assert total_values == unique_values

def test_sum_broad_major_all_state_non_empty():
    """
    Check that there are no rows with empty strings for total students for any
    state.
    """
    dataframe = pd.read_csv('broader_major_summed_data.csv', header=[0])
    assert dataframe["Students"].isnull().values.any() is False

def test_sum_broad_major_all_state_length():
    """
    Check that there are no repeats for any state by checking the length of
    the csv and ensuring that it matches what is expected.
    """
    dataframe = pd.read_csv('broader_major_summed_data.csv', header=[0])
    assert len(dataframe) == 1144

@pytest.mark.parametrize("major_name, total_students", \
    sum_broad_major_country_cases)
def test_sum_broad_major_country(major_name, total_students):
    """
    Check that common majors for all the states have been summed correctly
    through the function by checking that the csv created through the DataFrame
    returns the right value for the majors

    Args:
        major_name: A string representing the name of the major to be checked
        total_students: An integer representing the total number of students
            expected for the major given across the country
    """
    dataframe = pd.read_csv('broader_major_whole_country.csv',\
         header=[0]) #pylint: disable=E1136  # pylint/issues/3139
    df_this_major = dataframe.loc[dataframe["Major"] == major_name]
    assert df_this_major.iloc[0][1] == total_students

def test_sum_broad_major_country_non_empty():
    """
    Check that there are no rows with empty strings for total students for any
    major.
    """
    dataframe = pd.read_csv('broader_major_whole_country.csv', header=[0])
    assert dataframe["Students"].isnull().values.any() is False

def test_sum_broad_major_country_no_repeat():
    """
    Check that there are no repeats for any major.
    """
    dataframe = pd.read_csv('broader_major_whole_country.csv', header=[0])
    total_values = len(dataframe)
    unique_values = len(dataframe["Major"].unique())
    assert total_values == unique_values

def test_check_csvs():
    """
    Check that the last for each csv created is right.
    """
    df_one = pd.read_csv('broader_major_combined_data.csv', header=[0])
    check_one = (df_one.iloc[-1].values.tolist() == \
        ['wyoming','university-of-wyoming', 'Business', 63])

    df_two = pd.read_csv('broader_major_summed_data.csv', header=[0])
    check_two = (df_two.iloc[-1].values.tolist() == \
        ['wyoming', 'Business', 63])

    df_three = pd.read_csv('broader_major_whole_country.csv', header=[0])
    check_three = (df_three.iloc[-1].values.tolist() == \
        ['Architecture', 3581])
    assert check_one == check_two == check_three == True
