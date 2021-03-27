

def printFunction(med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_type_count_dict, individual_med_dict):


    """ Question 2 answers print"""
    print("\n")
    print("2a. med freq dict", med_freq_dict[:10])
    print("2b. med category freq dict", med_category_freq_dict[:10])

    """ Question 3 and 4 answers print"""
    print("3. individual_with_greatest_number_of_medication_types: ", individual_med_type_dict[:10])
    print("4. individual_with_least_number_of_medication_types: ", individual_med_type_dict[-10:])
    # print("3a. greatest medication type count: ", individual_med_type_count_dict[:10])
    # print("4a. least medication type count: ", individual_med_type_count_dict[-10:])

    """ Question 5 answers print"""
    print("5. individual_with_least_number_of_medications: ", individual_med_dict[-10:])
    print("\n")
