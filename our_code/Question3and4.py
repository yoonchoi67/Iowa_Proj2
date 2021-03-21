
def question3and4(row, individual_med_type_dict):
    if row[0] not in individual_med_type_dict:
        individual_med_type_dict[row[0]] = []
        individual_med_type_count_dict[row[0]] = 0
    if row[7] not in individual_med_type_dict[row[0]]:
        individual_med_type_dict[row[0]] += [row[7]]
        individual_med_type_count_dict[row[0]] +=1
    if row[8] not in individual_med_type_dict[row[0]]:
        individual_med_type_dict[row[0]] += [row[8]]
        individual_med_type_count_dict[row[0]] +=1
