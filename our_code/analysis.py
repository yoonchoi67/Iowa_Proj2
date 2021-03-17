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

    # skip the header, hence [1:]
    for row in reader[1:]:
        
        """ Question 2 code"""
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
    
        """ Question 3 and 4 code"""
        if row[0] not in individual_med_type_dict:
            individual_med_type_dict[row[0]] = []
        if row[7] not in individual_med_type_dict[row[0]]: individual_med_type_dict[row[0]] += [row[7]]

        """ Question 5 """

    """ Question 2 dictionaries sort """
    med_freq_dict = sorted(med_freq_dict.items(), key=lambda item: item[1], reverse=True)
    med_category_freq_dict = sorted(med_category_freq_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 3 and 4 dictionary sort """
    for k, v in individual_med_type_dict.items():
        #replace list with the count
        individual_med_type_dict[k]=len(v)
    individual_med_type_dict = sorted(individual_med_type_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 2 answers print"""
    print("med freq dict", med_freq_dict[:10])
    print("med category freq dict", med_category_freq_dict[:10])

    """ Question 3 and 4 answers print"""
    print("individual_with_greatest_number_of_medication_types: ", individual_med_type_dict[:10])
    print("individual_with_least_number_of_medication_types", individual_med_type_dict[-10:])