#count total records for each patient in xml, counts rows with duplicate patient_id
def question6b(row, individual_dict):
	if row[0] not in individual_dict:
		individual_dict[row[0]]=1
	elif row[0] in indivudal_dict:
		individual_dict[row[0]]+=1
