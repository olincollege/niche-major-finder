"""
"""
from collections import Counter
import pytest

from data_cleaning import (
    replace_major_with_broader_major,
    sum_common_broad_major_for_each_state,
    sum_common_broad_major_for_all_states,
    sum_common_broad_major_for_country,
)

# Define sets of test cases
replace_major_with_broader_major = [
    #
    (), 
]