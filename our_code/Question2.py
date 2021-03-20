
def question2(row, med_freq_dict, med_category_freq_dict):
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