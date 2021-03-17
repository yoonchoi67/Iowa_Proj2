import csv





med_freq_dict = {}
med_category_freq_dict = {}


with open("medication.csv", newline="", encoding="utf-8") as f:
    """["patient_id", "visit_id", "medication_id", "start", "end", "time", "text", "type1", "type2", "comment"]"""

    reader = list(csv.reader(f))

    # skip the header, hence [1:]
    for row in reader[1:]:
        
        """ Question 2 """
        # frequency distribution of medications taken
        if row[6] == "": pass
        elif row[6] not in med_freq_dict: med_freq_dict[row[6]] = 1
        else: med_freq_dict[row[6]] += 1
        # frequency distribution of categories of medications taken (type 1)
        if row[7] == "": pass
        elif row[7] not in med_category_freq_dict: med_category_freq_dict[row[7]] = 1
        else: med_category_freq_dict[row[7]] += 1
        # frequency distribution of categories of medications taken (type 1)
        if row[7] == "": pass
        elif row[8] not in med_category_freq_dict: med_category_freq_dict[row[8]] = 1
        else: med_category_freq_dict[row[8]] += 1
        
    med_freq_dict = sorted(med_freq_dict.items(), key=lambda item: item[1], reverse=True)
    med_category_freq_dict = sorted(med_category_freq_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 2 answers print"""
    print("med freq dict", med_freq_dict[:10])
    print("\n")
    print("med category freq dict", med_category_freq_dict[:10])