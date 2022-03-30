import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import geopandas
import pandas as pd

# Plot Major Ratios in a Bar Graph
data_set = pd.read_csv('broader_major_whole_country.csv', names = ["Major", "Students"])
major = data_set["Major"]
students = data_set["Students"]

plt.plot(major, students, ".")
plt.show()


##################

#states = geopandas.read_file('broader_major_summed_data.csv')
#type(states)

#states.head()

#states.crs

#states = states.to_crs("EPSG:3395")

#states.plot()