
def question2b(row, med_category_freq_dict):
    """ frequency distribution of medications category taken """

    # frequency distribution of categories of medications taken (type 1)
    if row[7] == "": pass
    elif row[7] not in med_category_freq_dict: med_category_freq_dict[row[7]] = 1
    else: med_category_freq_dict[row[7]] += 1
    
    # frequency distribution of categories of medications taken (type 2)
    if row[8] == "": pass
    elif row[8] not in med_category_freq_dict: med_category_freq_dict[row[8]] = 1
    else: med_category_freq_dict[row[8]] += 1