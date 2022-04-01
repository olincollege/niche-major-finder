"""
This file contains the functions needed to clean the data collected through web
scraping. In order to run these functions, first it is necessary to navigate
to the directory containing the raw data to be cleaned.
"""
import os
import glob
import pandas as pd


def files_to_df():
    """
    This function combines all csv files from the current folder into one csv.
    """
    all_filenames = sorted(list(glob.glob("*.{}".format("csv"))))
    combined_data = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_data.to_csv("combined_data.csv", index=False,
                         encoding="utf-8-sig")


def get_key(value_to_find, dictionary):
    """
    This function finds the key corresponding to a specific value in a
    dicionary.

    Args:
        value_to_find: A value that is being searched for in the dictionary.
            For this application, this value is a list of majors that correspond
            to the broader major name
        dict: A dictionary that contains one or more keys and values.

    Returns:
    A string representing the key in the dictionary that has the input as its
    value.
    """
    for key, value in dictionary.items():
        if value_to_find == value:
            return key
    return None


def find_broader_major(major_entered):
    """
    This function finds the condensed major name of the input major based on
    the major category created.

    The dictionary containing all majors and what broader name they correspond
    to was created through manual sorting. It contains all majors in the current
    raw_data folder. However, if further data is pulled from outside of
    raw_data, the dictionary might need to be changed manually.

    Args:
        major_entered: A string representing the name of a specific major for
                        which the broader category is to be found.

    Returns:
    A string representing the condensed category of the input major.
    """
    # Dictionary that maps majors to broader categories
    # This was hand sorted for data in the current raw_data folder

    broader_major_dict = {
        "Engineering": ["Bioengineering and Biomedical Engineering",
                        "Biotechnology", "Environmental Engineering",
                        "Chemical Engineering",
                        "Materials Engineering", "Mechanical Engineering",
                        "Engineering",
                        "Drafting and Design (CAD/CADD)",
                        "Engineering Science", "Industrial Engineering",
                        "Systems Engineering", "Industrial and Product Design",
                        "Robotics and Automation Engineering Technician",
                        "Electrical Engineering",
                        "Computer Hardware Engineering",
                        "Robotics and Automation Engineering",
                        "Aerospace Engineering",
                        "Aeronautics and Aviation Technology",
                        "Military Systems Technology"],
        "Computer Science": ["Computer Science",
                             "Computer Software Engineering",
                             "Information Technology",
                             "Computer Programming", "Data Processing",
                             "Computer and Information Sciences",
                             "Human Computer Interaction",
                             "Computer Systems Networking and " +
                             "Telecommunications",
                             "Network, Database, and System Administration",
                             "Computer and Information Systems Security",
                             "Computer Engineering Technician",
                             "Systems Science and Theory"],
        "Science": ["Physical Sciences", "Physics", "Engineering Physics",
                    "Chemistry", "Apparel and Textile Science",
                    "Pharmacology and Toxicology", "Bioinformatics",
                    "Cellular Biology",
                    "Biology", "Biochemistry and Molecular Biology",
                    "Ecology and Evolutionary Biology", "Microbiology"],
        "Math": ["Mathematics", "Computational and Applied Mathematics",
                 "Statistics"],
        "Psychology": ["Psychology", "Physiological Psychology",
                       "Research and Experimental Psychology",
                       "Counseling Psychology",
                       "Psychiatric and Mental Health Services",
                       "Developmental and Child Psychology",
                       "Social Psychology",
                       "Human Development", "Mental and Social Health Services",
                       "Community Health Services and Counseling",
                       "Marriage and Family Therapy and Counseling",
                       "Cognitive Science"],
        "Agriculture and Environment": ["Agricultural Business",
                                        "Animal Sciences and Husbandry",
                                        "Horticulture", "Agriculture",
                                        "Veterinary Technician and Assistant",
                                        "Equine Studies",
                                        "Plant Science",
                                        "Agricultural Production Operations",
                                        "Crop and Soil Sciences",
                                        "Agricultural Teacher Education",
                                        "Agricultural and Food Products" +
                                        " Processing",
                                        "Agricultural Engineering",
                                        "Agricultural Mechanics and Machinery",
                                        "Sustainability Studies",
                                        "Environmental Science",
                                        "Wildlife and Fisheries Management",
                                        "Natural Resources Conservation and " +
                                        "Management",
                                        "Zoology and Entomology",
                                        "Marine Science",
                                        "Atmospheric Sciences and Meteorology",
                                        "Geology and Earth Science",
                                        "Geography",
                                        "Marine Biology and Oceanography",
                                        "Natural Sciences",
                                        "Landscaping and Groundskeeping"],
        "Health Science": ["Biomedical Sciences and Molecular Medicine",
                           "Public Health",
                           "Health Service Preparatory Studies",
                           "Physiology and Pathology",
                           "Neuroscience and Neurobiology",
                           "Anatomy", "Health Professions",
                           "Pre-Medicine Studies",
                           "Alternative Medicine and Holistic Health",
                           "Optometry",
                           "Communication Disorders",
                           "Foods, Nutrition, and Wellness Studies",
                           "Dietetics and Clinical Nutrition",
                           "Speech Language Pathology"],
        "Physical Therapy": ["Exercise Physiology",
                             "Kinesiology and Exercise Science",
                             "Occupational Therapist Assistant",
                             "Physical Therapy Technician", "Physical Therapy",
                             "Occupational Therapy",
                             "Rehabilitation and Therapy"],
        "Nursing": ["Nursing", "Licensed Practical Nurse Training (LPN)",
                    "Nursing Assistant",
                    "Nursing Science, Education, and Practice",
                    "Adult Health Nursing",
                    "Family Practice and Pediatric Nursing",
                    "Emergency Care Attendant (EMT)", "Medical Assistant",
                    "Health Aides and Attendants", "Physician Assistant",
                    "Dental Assisting"],
        "Medical Applied": ["Radiologic Technician",
                            "Sonographer and Ultrasound Technician",
                            "Respiratory Care Therapy",
                            "Emergency Medical Technician (EMT Paramedic)",
                            "Phlebotomy Technician", "Radiation Therapy",
                            "Medical Technician", "Cardiovascular Technician",
                            "Medical Laboratory Technician",
                            "Occupational Safety and Health Technician",
                            "Surgical Technologist",
                            "Lab Technician", "Dental Hygiene",
                            "Medical Records Technician",
                            "Medical Insurance Coding",
                            "Pharmacy Technician",
                            "Pharmacy and Pharmaceutical Sciences"],
        "Trade Engineering":
        ["HVAC and Refrigeration Engineering Technician", "Welding",
         "Mining and Petroleum Engineering", "General Construction Trades",
         "Heavy Equipment Maintenance Technician", "Machine and Metal Working",
         "Construction Engineering Technician", "Carpentry",
         "Mechanical Engineering Technician", "Engineering Technician",
         "Mechanics and Repair", "Civil Engineering Technician",
         "Manufacturing Engineering Technician", "Automotive Mechanics",
         "Construction and Heavy Equipment Operation", "Diesel Mechanics",
         "Electrician", "Electrical Engineering Technician",
         "Electronics Equipment Installation and Repair",
         "Computer Systems Technician", "Instrumentation Technician",
         "Aerospace Engineering Technician", "Aircraft Maintenance"],
        "Trade Other": ["Cosmetology", "Esthetician and Skin Care",
                        "Massage Therapy and Bodywork", "Air Transportation",
                        "Professional Pilot",
                        "Truck,  Bus, and Commercial Vehicle Operation",
                        "Ground Transportation", "Child Development",
                        "Child Care Provider"],
        "Arts": ["Arts", "Studio Arts", "Visual and Performing Arts",
                 "Art History", "Photography", "Illustration", "Fine Arts",
                 "Commercial and Advertising Art", "Commercial Photography",
                 "Painting",
                 "Sculpture", "Fashion and Apparel Design", "Multimedia",
                 "Computer Graphics", "Music Theory and Composition", "Music",
                 "Music History and Literature", "Music Teacher Education",
                 "Music Management", "Musical Instruments",
                 "Animation, Video Graphics and Special Effects",
                 "Digital Communication and Media/Multimedia",
                 "Film and Video Studies",
                 "Graphic Design", "Web Page and Digital Design",
                 "Game Design and Interactive Media", "Acting",
                 "Theatre Design", "Dance", "Drama and Theatre Production",
                 "Voice and Opera", "Conducting", "Music Performance",
                 "Cinematography and Video Production"],
        "Culinary": ["Culinary Arts and Food Service",
                     "Family Studies and Consumer Sciences",
                     "Baking and Pastry Arts"],
        "Architecture": ["Architectural Engineering", "Interior Architecture",
                         "Architectural Engineering Technician",
                         "Architecture",
                         "Interior Design", "Surveying Technician",
                         "Urban, Community and Regional Planning",
                         "Civil Engineering"],
        "Business": ["Business", "Business Support Services",
                     "International Business", "Entrepreneurship",
                     "Real Estate"],
        "Finance": ["Finance", "Banking and Finance", "Actuarial Science"],
        "Economics": ["Economics", "Managerial Economics"],
        "Marketing": ["Marketing", "Merchandising and Buying Operations",
                      "Advertising", "Fashion and Apparel Merchandising",
                      "Insurance"],
        "Accounting": ["Accounting", "Accounting Technician and Bookkeeping"],
        "Law": ["Paralegal", "Legal Studies",
                "Political Science and Government", "Public Policy Analysis"],
        "Crime and Military": ["Police and Criminal Science",
                               "Cyber/Computer Forensics and Counterterrorism",
                               "Criminal Justice and Law Enforcement " +
                               "Administration",
                               "Criminal Justice and Safety Studies",
                               "Criminology",
                               "Criminal Justice and Corrections",
                               "Forensic Science and Technology",
                               "Intelligence",
                               "Homeland Security and Disaster Management",
                               "Fire Science and Fire Fighting",
                               "Military Science",
                               "Fire Protection and Prevention"],
        "International Relations": ["International Relations",
                                    "International Studies",
                                    "Peace Studies and Conflict Resolution"],
        "Education": ["Physical Education Teaching and Coaching",
                      "Elementary Education", "Education",
                      "High School Education",
                      "Early Childhood Education",
                      "Middle School Education",
                      "Special Education and Teaching",
                      "Health Teacher Education",
                      "Kindergarten and Preschool Education",
                      "English and Speech Teacher Education",
                      "Art Teacher Education",
                      "Education Research and Evaluation",
                      "Public Health Education",
                      "Athletic Training"],
        "Management": ["Logistics and Supply Chain Management",
                       "Healthcare Management",
                       "Management Sciences and Information Systems",
                       "Hospitality and Tourism Management",
                       "Small Business Management",
                       "Office Management", "Human Resources",
                       "Construction Management",
                       "Operations Management", "Nursing Administration",
                       "Sport and Fitness Management",
                       "Medical Office Management",
                       "Property Management", "Hospital Management",
                       "Fine and Studio Arts Management",
                       "Aviation Management and Operations"],
        "Social Work": ["Social Work and Youth Services",
                        "Medical Social Work", "Family and Community Services",
                        "Human Services",
                        "Parks, Recreation and Leisure Studies",
                        "Public Administration",
                        "Community Organization and Advocacy"],
        "Communication": ["Information Science", "Communications",
                          "Journalism", "Public Relations",
                          "Radio and Television",
                          "Corporate Communications", "Graphic Communications",
                          "Radio and Television Broadcasting Technician",
                          "Design and Visual Communications"],
        "History and World Studies": ["History", "North American Studies",
                                      "European and Russian Studies"],
        "Anthropology": ["Anthropology", "Social Sciences",
                         "Urban Studies and Affairs", "Sociology",
                         "Social Science Research Methods",
                         "Organizational Behavior Studies",
                         "Behavioral Sciences"],
        "Humanities": ["Women\'s Studies", "Minority and Ethnic Studies",
                       "Philosophy", "Liberal Arts and Humanities"],
        "Language and Writing": ["English", "Literature", "Creative Writing",
                                 "Playwriting and Screenwriting",
                                 "Rhetoric and Composition",
                                 "Professional and Technical Writing",
                                 "Spanish Language and Literature",\
                                 "Foreign Languages and Literatures",
                                 "French Language and Literature",
                                 "Linguistics, Interpretation, and Translation",
                                 "Teaching English as a Second Language"],
        "Religion": ["Religious Studies", "Religious Vocations",
                     "Biblical Studies", "Theological and Ministerial Studies",
                     "Religious Education", "Missionary Studies",
                     "Divinity, Ministry, and Pre-Theology",
                     "Pastoral Counseling and Specialized Ministries"]}

    # Loop through each dict entry to find the major
    for this_major_list in broader_major_dict.values():
        if major_entered in this_major_list:
            return get_key(this_major_list, broader_major_dict)
    return None


def replace_major_with_broader_major(dataframe):
    """
    This function replaces all the specific major names with the broader
    major names in a dataframe

    Args:
        dataframe: A Pandas DataFrame containing a column called "Major" that
            has specific names for majors.

    Returns:
    A Pandas DataFrame where all specific major names in the column "Major" have
    been replaced with the broader version of the name.
    """
    index = 0

    # Replace specific major with broader major for all values in df
    while index < len(dataframe):
        dataframe["Major"][index] = \
            find_broader_major(dataframe["Major"][index])
        index += 1
    return dataframe


def sum_broad_major_per_state(dataframe, state_name):
    """
    This function sums the number of students in each college for unique majors
    for a single state.

    This function requires that the Pandas DataFrame entered has columns
    named "State", "Major", "Students" with the correct types.

    Args:
        dataframe: A Pandas DataFrame containing columns with the state name,
            college name, broad major name, and number of students enrolled in
            that major.
        state_name: A string representing a state name.

    Return:
    A list that contains nested lists containing the state name, the name of
    the major and the number of student enrolled in it. This will only return
    values for a single state.

        Example:
        [["alabama", "science", 54], ["alabama", "math", 32]]
    """
    # Create dataframe with data from state entered
    this_state_df = dataframe.loc[dataframe["State"] == state_name]

    # Find all majors in the state
    this_state_broad_majors = this_state_df["Major"].unique()

    this_state_summed = []

    # Create list with summed number of students in each major for the state
    for broad_major in this_state_broad_majors:
        this_major_df = this_state_df.loc[this_state_df["Major"]
                                          == broad_major]
        this_state_summed.append([state_name, broad_major,
                                  this_major_df["Students"].sum()])

    return this_state_summed


def sum_broad_major_all_states(dataframe):
    """
    This function provides the sum of number of students that major in a
    certain subject for all states in the DataFrame entered.

    Args:
        dataframe: The Pandas DataFrame that contains columns with the state
            names, college names, major names, and number of students enrolled
            in that major.

    Returns:
    A list that contains nested lists containing the state name, the name of
    the major and the number of student enrolled in it. This will return values
    for all states in the DataFrame entered.

        Example:
        [["alabama", "science", 54], ["alaska", "math", 23]]
    """
    # Find all states in df
    all_states = dataframe["State"].unique()

    all_state_summed = []

    # Create list with summed number of students in a major for every state
    for state in all_states:
        this_state_summed = sum_broad_major_per_state(dataframe, state)
        all_state_summed = all_state_summed + this_state_summed

    return all_state_summed


def sum_broad_major_country(dataframe):
    """
    This function sums the total number of students in all states that chose
    a specific major.

    Args:
        dataframe: A Pandas DataFrame that contains columns with state names,
            major names, and the number of student in the state enrolled in the
            major.

    Returns:
    A list containing nested lists with the name of majors and the total number
    of student in the DataFrame enrolled in the major.
    """
    # Find all majors in df
    all_majors = dataframe["Major"].unique()

    country_summed = []

    # Create list with total students across all states majoring in each major
    for major in all_majors:
        this_major_df = dataframe.loc[dataframe["Major"] == major]
        country_summed.append([major, this_major_df["Students"].sum()])

    return country_summed


def create_csvs(dataframe):
    """
    This function creates three csvs for further visualization.

    1. Contains all data from `combined_data.csv`, replaces major names with
       broader categories. Done by calling replace_major_with_broader_major

    2. Sums students in each state with certain major. Done by calling
       sum_broad_major_all_states

    3. Sums students across America with certain major. Done by calling
       sum_broad_major_country

    Args:
        dataframe: A Pandas DataFrame that contains columns with state names,
            major names, and the number of student in the state enrolled in the
            major.
    """
    # Create csv with broader majors in place of specific majors
    broader_df = replace_major_with_broader_major(dataframe)
    broader_df.to_csv("broader_major_combined_data.csv", index=False,
                      encoding="utf-8-sig")

    # Create csv with total students in same major summed for each state
    broader_summed = sum_broad_major_all_states(broader_df)
    broader_summed_df = pd.DataFrame(broader_summed, columns=["State", "Major",
                                                              "Students"])
    broader_summed_df.to_csv("broader_major_summed_data.csv", index=False,
                             encoding="utf-8-sig")

    # Create csv with total students in same major across all states summed
    country_summed = sum_broad_major_country(broader_df)
    country_summed_df = pd.DataFrame.from_dict(
        country_summed, orient="columns")
    country_summed_df.columns = ["Major", "Students"]
    country_summed_df.to_csv("broader_major_whole_country.csv", index=False,
                             encoding="utf-8-sig")
"""
# Remove previous attempts
# os.chdir("testing")
os.chdir("raw_data")
os.remove("combined_data.csv")

# Combine data files for all states in folder and read to Pandas DataFrame
files_to_df()
df = pd.read_csv("combined_data.csv")

# Remove previous attempts
os.chdir("..")
# os.mkdir("cleaned_data")
os.chdir("cleaned_data")
#os.remove("broader_major_combined_data.csv")
#os.remove("broader_major_summed_data.csv")
#os.remove("broader_major_whole_country.csv")

# Create cleaned csv files
create_csvs(df)
"""