
def question2a(row, med_freq_dict):
    """ frequency distribution of medications taken """
    """ Overlap with before, during, and after DTC """
    # if row[6] == "": pass #14312 of these are empty because their med_id starts with DOC.
    if row[6] not in med_freq_dict: med_freq_dict[row[6]] = 1
    else: med_freq_dict[row[6]] += 1
