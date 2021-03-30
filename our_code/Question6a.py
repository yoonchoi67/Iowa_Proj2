#create list of unique visit ids for each patient
#count amount of unique visit ids for each patient

def question6a(row, individual_dict, individual_visit_count_dict):
	if row[0] not in individual_dict:
		individual_dict[row[0]]=[]
		individual_visit_count_dict[row[0]]=0
	if row[1] not in individual_dict[row[0]]:
		individual_dict[row[0]]+=[row[1]]
		individual_visit_count_dict[row[0]]+=1
