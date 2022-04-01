"""
Test functions in data_visualization.py are working properly.
"""
import os
import geopandas
import pytest
import data_cleaning

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_visualization import (
    total_students_per_state,
    students_in_a_major_per_state,
    
)

total_students_per_state_cases  = [


]

students_in_a_major_per_state_cases



@pytest.mark.parametrize("specific_major, broader_major", \
                                                total_students_per_state_cases)
def test_total_students_per_state():
    """
    Check that function total_students_per_state correctly coverts a datafram
    file to a list.
    """
    os.chdir("raw_data")
    dataframe = pd.read_csv("combined_data.csv", header=[0])
    assert (dataframe[1529:1568].loc["Student"] ==
            [3266])


@pytest.mark.parametrize("specific_major, broader_major", \
                                            students_in_a_major_per_state_cases)
def test_students_in_a_major_per_state():
    """
    Check that function students_in_a_major_per_state correctly creates a list
    of the numbers of students enrolled in a major for all states.
    """
    dataframe = pd.read_csv("combined_data.csv", header=[0])
    assert (dataframe.iloc[1].values.tolist() ==
            [ ])






