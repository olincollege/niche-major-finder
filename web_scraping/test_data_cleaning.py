from collections import Counter
from matplotlib import testing
import data_cleaning
import pytest
import pandas as pd
import os

"""
Test functions in data_cleaning.py are working properly.
"""

from data_cleaning import (
    get_key,
    find_broader_major,
    replace_major_with_broader_major,
    sum_broad_major_per_state,
    sum_broad_major_country,
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

"""
replace_major_with_broader_major = [
    (hawaii_and_idaho,)

]
"""

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("value_entered, dict, key_name", get_key_cases)
def test_get_key(value_entered, dict, key_name):
    """
    Check that get_key returns the key that corresponds to the input value.

    Args:
        value: A string that is one of the value in a dictionary
        testing_dict: A string representing the key that correspond to the input
                      value.
    """
    assert get_key(value_entered, dict) == key_name

@pytest.mark.parametrize("specific_major, broader_major", find_broader_major_cases)
def test_find_broader_major(specific_major, broader_major):
    """
    Check that get_key returns the key which is the condensed major name when
    the input is a specific major name.

    Args:
        value: A string representing the specific major name.
        testing_dict: A string representing the condensed major name.
        
    """
    assert find_broader_major(specific_major) == broader_major

"""
@pytest.mark.parametrize("value, testing_dict", find_broader_major)
    def test_replace_major_with_broader_major(value, testing_dict):


"""


