
def sortEverything(med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_type_count_dict, individual_med_dict, individual_visit_count_dict):
    """ Question 2 dictionaries sort """
    med_freq_dict = sorted(med_freq_dict.items(), key=lambda item: item[1], reverse=True)
    med_category_freq_dict = sorted(med_category_freq_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 3 and 4 dictionary sort """
    for k, v in individual_med_type_dict.items():
        #replace list with the count
        individual_med_type_dict[k]=len(v)
    individual_med_type_dict = sorted(individual_med_type_dict.items(), key=lambda item: item[1], reverse=True)

    # """ Question 3a and 4a dictionary sort """
    for k, v in individual_med_type_count_dict.items():
        #replace list with the count
        individual_med_type_count_dict[k]=v
    individual_med_type_count_dict = sorted(individual_med_type_count_dict.items(), key=lambda item: item[1], reverse=True)

    """ Question 5 dictionaries sort """
    for k, v in individual_med_dict.items():
        #replace list with the count
        individual_med_dict[k]=len(v)
    individual_med_dict = sorted(individual_med_dict.items(), key=lambda item: item[1])

    """ Question 6 dictionaries sort """
    individual_visit_count_dict = sorted(individual_visit_count_dict.items(), key=lambda item: item[1], reverse=True)

    

    return [med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_type_count_dict, individual_med_dict, individual_visit_count_dict]