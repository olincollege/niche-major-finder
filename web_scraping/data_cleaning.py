import pandas as pd
import os
import glob

def files_to_df():
    """
    This function __FINISH__
    Args:
        folder_name:

    Returns:

    """
    os.chdir("raw_data")
    all_filenames = sorted([i for i in glob.glob("*.{}".format("csv"))])
    print(all_filenames)
    combined_data = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv = combined_data.to_csv("combined_data.csv", index=False, encoding="utf-8-sig")

def find_condensed_major(major_entered):
    """
    """
    condensed_major_dic = {"Bioengineering": ['Bioengineering and Biomedical Engineering', 'Biotechnology', 'Environmental Engineering'
]}


# files_to_df()
df = pd.read_csv("combined_data.csv")
unique_majors = df['Major'].unique()

for major_entry in df['Major']:

