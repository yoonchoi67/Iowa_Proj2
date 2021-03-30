import csv
import xml_to_csv, Question2a, Question2b, Question3and4, Question5, Question6a, SortModule, PrintModule, CsvModule

""" Question 2a dictionary"""
med_freq_dict = {}
""" Question 2b dictionary"""
med_category_freq_dict = {}
""" Question 3 and 4 dictionaries"""
individual_med_type_dict = {}
individual_med_type_count_dict = {}
""" Question 5 dictionaries"""
individual_med_dict = {}
""" Question 6 dictionaries"""
individual_dict = {}
individual_visit_count_dict = {}

def parseFunction():
    with open("medication.csv", newline="", encoding="utf-8") as f:
        """["patient_id", "visit_id", "medication_id", "start", "end", "time", "text", "type1", "type2", "comment"]"""

        med_id_has_DOC = False
        med_id_first_M = False
        intermerdiate_medicines = []

        reader = list(csv.reader(f))
        
        # skip the header, hence [1:]
        for row in reader:
            
            """ Looks if medication_id starts with DOC or the first of M after DOC """
            if "M" in row[2] and med_id_has_DOC: med_id_first_M = True
            else: med_id_first_M = False
            if "DOC" in row[2]: 
                med_id_has_DOC = True
                # clear the medicine entries
                intermerdiate_medicines = []
            else: med_id_has_DOC = False

            # """ Questions that only need the first of the 'M' type in med_id"""
            # if med_id_first_M:
                # """ Question 2a code """
                # Question2a.question2a(row, med_freq_dict)
                # """ Question 5 code """
                # Question5.question5(row, individual_med_dict)

            """ Questions that loops through only those with 'M' type in med_id"""
            if not med_id_has_DOC:
                # if there are duplicate medication names with med_id with 'M' and under the same 'DOC', skip
                if row[6] in intermerdiate_medicines:
                    pass
                else:
                    intermerdiate_medicines.append(row[6])
                    """ Question 2a code """
                    Question2a.question2a(row, med_freq_dict)
                    """ Question 5 code """
                    Question5.question5(row, individual_med_dict)

            """ Questions that only need the 'DOC' type in med_id"""
            if med_id_has_DOC:
                """ Question 2b code """
                Question2b.question2b(row, med_category_freq_dict)    
                """ Question 3 and 4 code """
                Question3and4.question3and4(row, individual_med_type_dict, individual_med_type_count_dict)

            """ Question 6 code """
            Question6a.question6a(row, individual_dict, individual_visit_count_dict)

def main():
    """ change xml to csv if medication.csv doesn't exist """
    # xml_to_csv
    
    """ analysis for questions """
    parseFunction()

    """ sort the answers from parseFunction """
    #answers[0] = med_freq_dict, a[1] = med_category_freq_dict, a[2] = individual_med_type_dict, answers[3] = individual_med_type_count_dict, a[4] = individual_med_dict
    answers = SortModule.sortEverything(
        med_freq_dict, 
        med_category_freq_dict,
        individual_med_type_dict, 
        individual_med_type_count_dict, 
        individual_med_dict,
        individual_visit_count_dict
        )

    """ print the answers from sortFunction() """
    # a[0] = med_freq_dict, a[1] = med_category_freq_dict, a[2] = individual_med_type_dict, answers[3] = individual_med_type_count_dict, a[4] = individual_med_dict
    PrintModule.printFunction(answers[0], answers[1], answers[2], answers[3], answers[4], answers[5])

    """ store the answers to csv """
    CsvModule.csvFunction(answers[0], answers[1], answers[2], answers[3], answers[4], answers[5])

if __name__ == "__main__":
    main() 
