import csv



""" Question 3 and 4 dictionaries"""
individual_med_type_dict = {}
new_individual_med_type_dict = {}

with open("medication.csv", newline="", encoding="utf-8") as f:
    """["patient_id", "visit_id", "medication_id", "start", "end", "time", "text", "type1", "type2", "comment"]"""

    reader = list(csv.reader(f))

    # skip the header, hence [1:]
    for row in reader[1:]:
        if row[0] not in individual_med_type_dict:
            individual_med_type_dict[row[0]] = {}
        if row[7] not in individual_med_type_dict[row[0]]: individual_med_type_dict[row[0]][row[7]] = 1
        else: individual_med_type_dict[row[0]][row[7]] += 1

    for k, v in individual_med_type_dict.items():
        v = sorted(v.items(), key=lambda item: item[1], reverse=True)
        new_individual_med_type_dict[k]=v
    new_individual_med_type_dict = sorted(new_individual_med_type_dict.items(), key=lambda item: item[0])

    print("\n")
    print("new_individual_med_type_dict", new_individual_med_type_dict)