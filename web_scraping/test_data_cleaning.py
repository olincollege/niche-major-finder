"""
"""
from collections import Counter
import pytest

from data_cleaning import (
    get_key,
    find_broader_major,
    replace_major_with_broader_major,
    sum_broad_major_per_state,
    sum_broad_major_country,
)

testing_dict = {'Computer Science': ['Computer Science',\
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
    'Agriculture and Environment': ['Agricultural Business',\
    'Animal Sciences and Husbandry', 'Horticulture', 'Agriculture', \
    'Veterinary Technician and Assistant', 'Equine Studies', \
    'Plant Science', 'Agricultural Production Operations',\
    'Crop and Soil Sciences', 'Agricultural Teacher Education', \
    'Agricultural and Food Products Processing', \
    'Agricultural Engineering', 'Agricultural Mechanics and Machinery', \
    'Sustainability Studies', 'Environmental Science', \
    'Wildlife and Fisheries Management', \
    'Natural Resources Conservation and Management', \
    'Zoology and Entomology', 'Marine Science', \
    'Atmospheric Sciences and Meteorology', 'Geology and Earth Science', \
    'Geography', 'Marine Biology and Oceanography', 'Natural Sciences', \
    'Landscaping and Groundskeeping']}

# Define sets of test cases
get_key = [
    # Check for key in the dictionary
    (, testing_dict), 
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("value,testing_dict", get_key)
