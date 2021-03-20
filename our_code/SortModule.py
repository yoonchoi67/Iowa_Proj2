
def sortEverything(med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_dict):
    """ Question 2 dictionaries sort """
    med_freq_dict = sorted(med_freq_dict.items(), key=lambda item: item[1], reverse=True)
    med_category_freq_dict = sorted(med_category_freq_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 3 and 4 dictionary sort """
    for k, v in individual_med_type_dict.items():
        #replace list with the count
        individual_med_type_dict[k]=len(v)
    individual_med_type_dict = sorted(individual_med_type_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 5 dictionaries sort """
    for k, v in individual_med_dict.items():
        #replace list with the count
        individual_med_dict[k]=len(v)
    individual_med_dict = sorted(individual_med_dict.items(), key=lambda item: item[1])

    return [med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_dict]