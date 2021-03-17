import csv




""" Question 2 dictionaries"""
med_freq_dict = {}
med_category_freq_dict = {}
""" Question 3 and 4 dictionaries"""
individual_med_type_dict = {}
""" Question 5 dictionaries"""
individual_med_dict = {}

with open("medication.csv", newline="", encoding="utf-8") as f:
    """["patient_id", "visit_id", "medication_id", "start", "end", "time", "text", "type1", "type2", "comment"]"""

    reader = list(csv.reader(f))

    row6 = 0
    row7 = 0
    row8 = 0
    # skip the header, hence [1:]
    for row in reader[1:]:
        
        """ Question 2 """
        # frequency distribution of medications taken
        if row[6] == "": pass #14312 of these empty
        elif row[6] not in med_freq_dict: med_freq_dict[row[6]] = 1
        else: med_freq_dict[row[6]] += 1
        # frequency distribution of categories of medications taken (type 1)
        if row[7] == "": pass #0 of these empty
        elif row[7] not in med_category_freq_dict: med_category_freq_dict[row[7]] = 1
        else: med_category_freq_dict[row[7]] += 1
        # frequency distribution of categories of medications taken (type 1)
        if row[8] == "": pass #61297 of these empty
        elif row[8] not in med_category_freq_dict: med_category_freq_dict[row[8]] = 1
        else: med_category_freq_dict[row[8]] += 1
    
        """ Question 3 """
        # if row[0] not in individual_med_type_dict:  

        """ Question 4 """
        """ Question 5 """

    """ Question 2 dictionaries """
    med_freq_dict = sorted(med_freq_dict.items(), key=lambda item: item[1], reverse=True)
    med_category_freq_dict = sorted(med_category_freq_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 2 answers print"""
    print("med freq dict", med_freq_dict[:10])
    print("\n")
    print("med category freq dict", med_category_freq_dict[:10])