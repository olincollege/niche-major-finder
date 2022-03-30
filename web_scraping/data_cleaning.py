from dataclasses import replace
import pandas as pd
import os
import glob
import csv

def files_to_df():
    """
    This function combines all .csv files from the current folder in to one.

    """
    all_filenames = sorted([i for i in glob.glob("*.{}".format("csv"))])
    print(all_filenames)
    combined_data = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_data.to_csv("combined_data.csv", index=False, encoding="utf-8-sig")

def get_key(value_to_find, dict):
    """
    This function looks for a specific value in a dicionary and returns all of
    its key.

    Args:
    value_to_find: A string that is being searched in the dictionary.
    dict: A dictionary that contains one or more keys and values.

    Return:
    key: A string that is the key corresponding to the input value.

    """
    for key, value in dict.items():
        if value_to_find == value:
            return key
    return None

def find_broader_major(major_entered):
    """
    This function finds the condensed major name of the input major based on
    the major category created.

    Arg:
    major_entered: A string that is the name of a specific major.

    Return:
    A string that is the condensed name version of the input major.

    """
    # Dictionary that maps majors to broader categories
    # This was hand sorted from the results of the unique majors
    broader_major_dict = {
        'Engineering': ['Bioengineering and Biomedical Engineering', \
        'Biotechnology', 'Environmental Engineering', 'Chemical Engineering', \
        'Materials Engineering', 'Mechanical Engineering', 'Engineering', \
        'Drafting and Design (CAD/CADD)',\
        'Engineering Science', 'Industrial Engineering',\
        'Systems Engineering', 'Industrial and Product Design',\
        'Robotics and Automation Engineering Technician', \
        'Electrical Engineering', 'Computer Hardware Engineering', \
        'Robotics and Automation Engineering', 'Aerospace Engineering', \
        'Aeronautics and Aviation Technology', 'Military Systems Technology'], 
        'Computer Science': ['Computer Science',\
        'Computer Software Engineering', 'Information Technology', \
        'Computer Programming', 'Data Processing', \
        'Computer and Information Sciences', 'Human Computer Interaction', \
        'Computer Systems Networking and Telecommunications', \
        'Network, Database, and System Administration', \
        'Computer and Information Systems Security', \
        'Computer Engineering Technician', 'Systems Science and Theory'], 
        'Physical Sciences': ['Physics', 'Engineering Physics', \
        'Physical Sciences', 'Chemistry', 'Apparel and Textile Science', \
        'Pharmacology and Toxicology'], 
        'Math': ['Mathematics', 'Computational and Applied Mathematics', \
        'Statistics'], 
        'Biology': ['Bioinformatics', 'Cellular Biology', 'Biology',\
        'Biochemistry and Molecular Biology', \
        'Ecology and Evolutionary Biology', 'Microbiology'], 
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
        'Landscaping and Groundskeeping'], 
        'Health Science': ['Biomedical Sciences and Molecular Medicine', \
        'Public Health', 'Health Service Preparatory Studies', \
        'Physiology and Pathology', 'Neuroscience and Neurobiology', \
        'Anatomy', 'Health Professions', 'Pre-Medicine Studies', \
        'Alternative Medicine and Holistic Health', 'Optometry', \
        'Communication Disorders', 'Foods, Nutrition, and Wellness Studies',\
        'Dietetics and Clinical Nutrition', 'Speech Language Pathology'],  
        'Physical Therapy': ['Exercise Physiology', \
        'Kinesiology and Exercise Science', 'Occupational Therapist Assistant',\
        'Physical Therapy Technician', 'Physical Therapy', \
        'Occupational Therapy', 'Rehabilitation and Therapy'], 
        'Nursing': ['Nursing', 'Licensed Practical Nurse Training (LPN)', \
        'Nursing Assistant', 'Nursing Science, Education, and Practice',\
        'Adult Health Nursing', 'Family Practice and Pediatric Nursing', \
        'Emergency Care Attendant (EMT)', 'Medical Assistant', \
        'Health Aides and Attendants', 'Physician Assistant', \
        'Dental Assisting'], 
        'Medical Applied': ['Radiologic Technician', \
        'Sonographer and Ultrasound Technician', 'Respiratory Care Therapy', \
        'Emergency Medical Technician (EMT Paramedic)', \
        'Phlebotomy Technician', 'Radiation Therapy',\
        'Medical Technician', 'Cardiovascular Technician', \
        'Medical Laboratory Technician', \
        'Occupational Safety and Health Technician', 'Surgical Technologist', \
        'Lab Technician', 'Dental Hygiene', 'Medical Records Technician', \
        'Medical Insurance Coding', \
        'Pharmacy Technician', 'Pharmacy and Pharmaceutical Sciences'], 
        'Trade Engineering': \
        ['HVAC and Refrigeration Engineering Technician', 'Welding', \
        'Mining and Petroleum Engineering', 'General Construction Trades',\
        'Heavy Equipment Maintenance Technician', 'Machine and Metal Working',\
        'Construction Engineering Technician', 'Carpentry', \
        'Mechanical Engineering Technician', 'Engineering Technician', \
        'Mechanics and Repair', 'Civil Engineering Technician', \
        'Manufacturing Engineering Technician', 'Automotive Mechanics', \
        'Construction and Heavy Equipment Operation', 'Diesel Mechanics', \
        'Electrician', 'Electrical Engineering Technician',\
        'Electronics Equipment Installation and Repair',\
        'Computer Systems Technician', 'Instrumentation Technician', 
        'Aerospace Engineering Technician', 'Aircraft Maintenance'], 
        'Trade Other': ['Cosmetology', 'Esthetician and Skin Care', \
        'Massage Therapy and Bodywork', 'Air Transportation', \
        'Professional Pilot', 'Truck,  Bus, and Commercial Vehicle Operation',\
        'Ground Transportation', 'Child Development', 'Child Care Provider'], 
        'Arts': ['Arts', 'Studio Arts', 'Visual and Performing Arts', \
        'Art History', 'Photography', 'Illustration', 'Fine Arts',\
        'Commercial and Advertising Art', 'Commercial Photography', 'Painting',\
        'Sculpture', 'Fashion and Apparel Design', 'Multimedia', \
        'Computer Graphics', 'Music Theory and Composition', 'Music', \
        'Music History and Literature', 'Music Teacher Education',\
        'Music Management', 'Musical Instruments', \
        'Animation, Video Graphics and Special Effects', \
        'Digital Communication and Media/Multimedia', 'Film and Video Studies',\
        'Graphic Design', 'Web Page and Digital Design', \
        'Game Design and Interactive Media', 'Acting', \
        'Theatre Design', 'Dance', 'Drama and Theatre Production', \
        'Voice and Opera', 'Conducting', 'Music Performance',\
        'Cinematography and Video Production'], 
        'Culinary': ['Culinary Arts and Food Service', \
        'Family Studies and Consumer Sciences', 'Baking and Pastry Arts'], 
        'Architecture': ['Architectural Engineering', 'Interior Architecture',\
        'Architectural Engineering Technician', 'Architecture', \
        'Interior Design', 'Surveying Technician', \
        'Urban, Community and Regional Planning', 'Civil Engineering'],
        'Business': ['Business', 'Business Support Services',\
        'International Business', 'Entrepreneurship', 'Real Estate'], 
        'Finance': ['Finance', 'Banking and Finance', 'Actuarial Science'],
        'Economics': ['Economics', 'Managerial Economics'], 
        'Marketing': ['Marketing', 'Merchandising and Buying Operations', \
        'Advertising', 'Fashion and Apparel Merchandising', 'Insurance'], 
        'Accounting': ['Accounting', 'Accounting Technician and Bookkeeping'], 
        'Law': ['Paralegal', 'Legal Studies', \
        'Political Science and Government', 'Public Policy Analysis'], 
        'Crime and Military': ['Police and Criminal Science', \
        'Cyber/Computer Forensics and Counterterrorism', \
        'Criminal Justice and Law Enforcement Administration', \
        'Criminal Justice and Safety Studies', 'Criminology', \
        'Criminal Justice and Corrections', 'Forensic Science and Technology',\
        'Intelligence', 'Homeland Security and Disaster Management', \
        'Fire Science and Fire Fighting', 'Military Science', \
        'Fire Protection and Prevention'], 
        'International Relations': ['International Relations', \
        'International Studies', 'Peace Studies and Conflict Resolution'], 
        'Education': ['Physical Education Teaching and Coaching', \
        'Elementary Education', 'Education', 'High School Education', \
        'Early Childhood Education', 'Middle School Education', \
        'Special Education and Teaching', 'Health Teacher Education',\
        'Kindergarten and Preschool Education', \
        'English and Speech Teacher Education', 'Art Teacher Education', \
        'Education Research and Evaluation', 'Public Health Education',\
        'Athletic Training'], 
        'Management': ['Logistics and Supply Chain Management', \
        'Healthcare Management', 'Management Sciences and Information Systems',\
        'Hospitality and Tourism Management', 'Small Business Management', \
        'Office Management', 'Human Resources', 'Construction Management', \
        'Operations Management', 'Nursing Administration', \
        'Sport and Fitness Management', 'Medical Office Management',\
        'Property Management', 'Hospital Management', \
        'Fine and Studio Arts Management', \
        'Aviation Management and Operations'],
        'Social Work': ['Social Work and Youth Services', \
        'Medical Social Work', 'Family and Community Services',\
        'Human Services', 'Parks, Recreation and Leisure Studies',\
        'Public Administration', 'Community Organization and Advocacy'],
        'Communication': ['Information Science', 'Communications', \
        'Journalism', 'Public Relations', 'Radio and Television',\
        'Corporate Communications', 'Graphic Communications', \
        'Radio and Television Broadcasting Technician', \
        'Design and Visual Communications'],
        'History and World Studies': ['History', 'North American Studies',\
        'European and Russian Studies'],
        'Anthropology': ['Anthropology', 'Social Sciences', \
        'Urban Studies and Affairs', 'Sociology', \
        'Social Science Research Methods', 'Organizational Behavior Studies',\
        'Behavioral Sciences'],
        'Humanities': ['Women\'s Studies', 'Minority and Ethnic Studies', \
        'Philosophy', 'Liberal Arts and Humanities'],
        'Language and Writing': ['English', 'Literature', 'Creative Writing',\
        'Playwriting and Screenwriting', 'Rhetoric and Composition', \
        'Professional and Technical Writing', \
        'Spanish Language and Literature', 'Foreign Languages and Literatures',\
        'French Language and Literature',\
        'Linguistics, Interpretation, and Translation',\
        'Teaching English as a Second Language'],
        'Religion': ['Religious Studies', 'Religious Vocations', \
        'Biblical Studies', 'Theological and Ministerial Studies', \
        'Religious Education', 'Missionary Studies', \
        'Divinity, Ministry, and Pre-Theology', \
        'Pastoral Counseling and Specialized Ministries']}
    
    for this_major_list in broader_major_dict.values():
        if major_entered in this_major_list:
            return get_key(this_major_list, broader_major_dict)

def replace_major_with_broader_major(df):
    """
    This function loops through a list and replaces all the elements which are
    specific major names with the condensed major names.

    Arg:
    df: A list of major names before being modified.

    Return:
    df: A list of major names with each name being replaced by the condensed
    version of major name.

    """
    i = 0
    while i < len(df):
        df['Major'][i] = find_broader_major(df['Major'][i])
        i += 1
    return df

def sum_common_broad_major_for_each_state(df, state_name):
    """
    This function takes a state name and look for it in the combined .csv file.
    It returns a list of different majors in this state and the number of
    students enrolled in that major.
    
    Args: 
    df: The .csv file that contains all states, colleges, majors, and number of
    students enrolled in that major.
    state_name: A string that is a state name.
    
    Return:
    this_state_summed: A list that contains all major names that show up in the
    input state and the number of student enrolled in these majors.

    """
    this_state_df = df.loc[df['State'] == state_name]
    this_state_broad_majors = this_state_df['Major'].unique()

    this_state_summed = []

    for broad_major in this_state_broad_majors:
        this_major_df = this_state_df.loc[this_state_df['Major'] == broad_major]
        this_state_summed.append([state_name, broad_major,\
             this_major_df['Students'].sum()])

    return this_state_summed

def sum_common_broad_major_for_all_states(df):
    """
    This function loops through all the states and produces lists of majors and
    number of students enrolled in that major for each state.
    
    Args:
    df: The .csv file that contains all states, colleges, majors, and number of
    students enrolled that major.
    all_state_summed: A list of lists with condenced major names, number of
    students enrolled in each major in each state, and each state name.

    Return:
    all_state_summed: a list with lists of majors and number of students
    enrolled in that major for each state.

    """
    all_states = df["State"].unique()
    all_state_summed = []

    for state in all_states:
        this_state_summed = sum_common_broad_major_for_each_state(df, state)
        all_state_summed = all_state_summed + this_state_summed

    return all_state_summed

def sum_common_broad_major_for_country(df):
    """
    This function loops through all majors in the .csv file, and creates a list
    with lists of majors and the total number of students enrolled in each major
    in the whole nation. 
    
    Args:
    df: The .csv file that contains all states, colleges, majors, and number of
    students enrolled that major.
    
    Return:
    country_summed: A list with lists of major names and student enrolled in
    each major.

    """
    all_majors = df["Major"].unique()

    country_summed = []

    for major in all_majors:
        this_major_df = df.loc[df["Major"] == major]
        country_summed.append([major, this_major_df['Students'].sum()])
    
    return country_summed

os.chdir("raw_data")
os.remove('combined_data.csv')
files_to_df() # --> to create combined_data.csv
df = pd.read_csv("combined_data.csv")

# unique_majors = df['Major'].unique() --> to find majors for categories - 
# manually sort
os.chdir('..')
os.chdir('cleaned_data')
#os.remove('broader_major_combined_data.csv')
#os.remove('broader_major_summed_data.csv')
#os.remove('broader_major_whole_country.csv')
os.chdir('..')
os.rmdir('cleaned_data')
os.makedirs('cleaned_data')
os.chdir('cleaned_data')

broader_df = replace_major_with_broader_major(df)
broader_df.to_csv("broader_major_combined_data.csv", index=False, \
    encoding="utf-8-sig")

broader_summed = sum_common_broad_major_for_all_states(broader_df)
broader_summed_df = pd.DataFrame(broader_summed, columns=['State', 'Major', \
    'Students'])
broader_summed_df.to_csv("broader_major_summed_data.csv", index=False,\
     encoding="utf-8-sig")

country_summed = sum_common_broad_major_for_country(broader_df)
country_summed_df = pd.DataFrame.from_dict(country_summed, orient='columns')
country_summed_df.columns=["Major", "Students"]
country_summed_df.to_csv("broader_major_whole_country.csv", index=False, \
    encoding="utf-8-sig")
