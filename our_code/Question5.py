
def question5(row, individual_med_dict):
    if row[0] not in individual_med_dict:
        individual_med_dict[row[0]] = []
    if row[6] not in individual_med_dict[row[0]]: individual_med_dict[row[0]] += [row[6]]