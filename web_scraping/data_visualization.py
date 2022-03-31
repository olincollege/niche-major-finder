import matplotlib.pyplot as plt
import numpy as np
import geopandas
import pandas as pd
import os

# Read CSV data into Pandas Dataframes
os.chdir('cleaned_data')
broader_major_summed_data_df = pd.read_csv("broader_major_summed_data.csv")
#print(broader_major_summed_data_df)
broader_major_whole_country_df = pd.read_csv('broader_major_whole_country.csv', names = ["Major", "Students"])

# Input # of students per major data into lists
major = broader_major_whole_country_df["Major"]
students = broader_major_whole_country_df["Students"]

majors_list = list(major[1:])
students_list = list(students[1:])

for i in range(0, len(students_list)):
    students_list[i] = int(students_list[i])

# Plot Number of Students in Each Major
def plot_number_of_students_per_major_USA():
    plt.barh(majors_list, students_list, align="center",alpha=.5)
    plt.title('Number of Students Enrolled in Different Majors Offered by the top 10% of Colleges in Each State')
    plt.xlabel('College Major')
    plt.ylabel('Number of Students Enrolled')
    plt.show()

# Create a List of All State Names
states_list = list(broader_major_summed_data_df['State'].unique())
####print(states_list)

# Order Majors by Popularity in the USA
broader_major_whole_country_df.sort_values(by=['Students'], inplace=True, ascending=False)
####print(broader_major_whole_country_df)

majors_by_descending_popularity = list(broader_major_whole_country_df["Major"])[1:]
####print(majors_by_descending_popularity)

# Create lists of the number of students enrolled in a major per state (create for all majors)

def students_in_a_major_per_state(major):

    y_current = []

    states_list = list(broader_major_summed_data_df['State'].unique())
    current_major_states_list = list(broader_major_summed_data_df.loc[broader_major_summed_data_df['Major'] == major, 'State'])

    #print(states_list)
    #print(current_major_states_list)

    i = 0

    while i < len(states_list):
        #print(states_list[i])
        if current_major_states_list.count(states_list[i]) == 0:
            #print(states_list[i])
            states_list[i] = 0
            i+=1
        else:
            i+=1

    for state in states_list:
        #print(state)
        if state != 0:
            #print(int(broader_major_summed_data_df.loc[(broader_major_summed_data_df['Major'] == major) & (broader_major_summed_data_df['State'] == state), 'Students']))
            #print(broader_major_summed_data_df.loc[(broader_major_summed_data_df['Major'] == major) & (broader_major_summed_data_df['State'] == state), 'Students'])
            y_current.append(int(broader_major_summed_data_df.loc[(broader_major_summed_data_df['Major'] == major) & (broader_major_summed_data_df['State'] == state), 'Students']))
        else:
            y_current.append(0)

    #print(y_current)
    return y_current

i = 0

students_in_a_major_per_state_all_majors = []

while i < len(majors_by_descending_popularity):
    #print(majors_by_descending_popularity[i])
    students_in_a_major_per_state_all_majors.append(students_in_a_major_per_state(majors_by_descending_popularity[i]))

    i +=1

#print(students_in_a_major_per_state_all_majors)

# Plot Major Ratios in a Stacked Bar Graph

def plot_major_ratios_in_stacked_bar_graph():
    
    y1 = np.array(students_in_a_major_per_state_all_majors[0])
    y2 = np.array(students_in_a_major_per_state_all_majors[1])
    y3 = np.array(students_in_a_major_per_state_all_majors[2])
    y4 = np.array(students_in_a_major_per_state_all_majors[3])
    y5 = np.array(students_in_a_major_per_state_all_majors[4])
    y6 = np.array(students_in_a_major_per_state_all_majors[5])
    y7 = np.array(students_in_a_major_per_state_all_majors[6])
    y8 = np.array(students_in_a_major_per_state_all_majors[7])
    y9 = np.array(students_in_a_major_per_state_all_majors[8])
    y10 = np.array(students_in_a_major_per_state_all_majors[9])
    y11 = np.array(students_in_a_major_per_state_all_majors[10])
    y12 = np.array(students_in_a_major_per_state_all_majors[11])
    y13 = np.array(students_in_a_major_per_state_all_majors[12])
    y14 = np.array(students_in_a_major_per_state_all_majors[13])
    y15 = np.array(students_in_a_major_per_state_all_majors[14])
    y16 = np.array(students_in_a_major_per_state_all_majors[15])
    y17 = np.array(students_in_a_major_per_state_all_majors[16])
    y18 = np.array(students_in_a_major_per_state_all_majors[17])
    y19 = np.array(students_in_a_major_per_state_all_majors[18])
    y20 = np.array(students_in_a_major_per_state_all_majors[19])
    y21 = np.array(students_in_a_major_per_state_all_majors[20])
    y22 = np.array(students_in_a_major_per_state_all_majors[21])
    y23 = np.array(students_in_a_major_per_state_all_majors[22])
    y24 = np.array(students_in_a_major_per_state_all_majors[23])
    y25 = np.array(students_in_a_major_per_state_all_majors[24])
    y26 = np.array(students_in_a_major_per_state_all_majors[25])
    y27 = np.array(students_in_a_major_per_state_all_majors[26])
    y28 = np.array(students_in_a_major_per_state_all_majors[27])
    y29 = np.array(students_in_a_major_per_state_all_majors[28])
    y30 = np.array(students_in_a_major_per_state_all_majors[29])
    y31 = np.array(students_in_a_major_per_state_all_majors[30])
    y32 = np.array(students_in_a_major_per_state_all_majors[31])

    # plot bars in stack manner
    plt.barh(states_list, y1, color='r')
    plt.barh(states_list, y2, left=y1)
    plt.barh(states_list, y3, left=y1+y2)
    plt.barh(states_list, y4, left=y1+y2+y3)
    plt.barh(states_list, y5, left=y1+y2+y3+y4)
    plt.barh(states_list, y6, left=y1+y2+y3+y4+y5)
    plt.barh(states_list, y7, left=y1+y2+y3+y4+y5+y6)
    plt.barh(states_list, y8, left=y1+y2+y3+y4+y5+y6+y7)
    plt.barh(states_list, y9, left=y1+y2+y3+y4+y5+y6+y7+y8)
    plt.barh(states_list, y11, left=y1+y2+y3+y4+y5+y6+y7+y8+y9)
    plt.barh(states_list, y12, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10)
    plt.barh(states_list, y13, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11)
    plt.barh(states_list, y14, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12)
    plt.barh(states_list, y15, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13)
    plt.barh(states_list, y16, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14)
    plt.barh(states_list, y17, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15)
    plt.barh(states_list, y18, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16)
    plt.barh(states_list, y19, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17)
    plt.barh(states_list, y20, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18)
    plt.barh(states_list, y21, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19)
    plt.barh(states_list, y22, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20)
    plt.barh(states_list, y23, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21)
    plt.barh(states_list, y24, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22)
    plt.barh(states_list, y25, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23)
    plt.barh(states_list, y26, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24)
    plt.barh(states_list, y27, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24+y25)
    plt.barh(states_list, y28, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24+y25+y26)
    plt.barh(states_list, y29, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24+y25+y26+y27)
    plt.barh(states_list, y30, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24+y25+y26+y27+y28)
    plt.barh(states_list, y31, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24+y25+y26+y27+y28+y29)
    plt.barh(states_list, y32, left=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15+y16+y17+y18+y19+y20+y21+y22+y23+y24+y25+y26+y27+y28+y29+y30)




    plt.xlabel("Number of Students Enrolled")
    plt.ylabel("State")
    plt.legend([majors_by_descending_popularity[0], majors_by_descending_popularity[1], majors_by_descending_popularity[2], majors_by_descending_popularity[3], majors_by_descending_popularity[4], majors_by_descending_popularity[5], majors_by_descending_popularity[6], majors_by_descending_popularity[7], majors_by_descending_popularity[8], majors_by_descending_popularity[9], majors_by_descending_popularity[10], majors_by_descending_popularity[11], majors_by_descending_popularity[12], majors_by_descending_popularity[13], majors_by_descending_popularity[14], majors_by_descending_popularity[15], majors_by_descending_popularity[16], majors_by_descending_popularity[17], majors_by_descending_popularity[18], majors_by_descending_popularity[19], majors_by_descending_popularity[20], majors_by_descending_popularity[21], majors_by_descending_popularity[22], majors_by_descending_popularity[23], majors_by_descending_popularity[24], majors_by_descending_popularity[25], majors_by_descending_popularity[26], majors_by_descending_popularity[27], majors_by_descending_popularity[28], majors_by_descending_popularity[29], majors_by_descending_popularity[30], majors_by_descending_popularity[31]])
    plt.title("Distribution of College Majors by State")
    plt.show()

plot_major_ratios_in_stacked_bar_graph()






















##################

#states = geopandas.read_file('broader_major_summed_data.csv')
#type(states)

#states.head()

#states.crs

#states = states.to_crs("EPSG:3395")

#states.plot()