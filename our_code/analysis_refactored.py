import csv
import xml_to_csv, Question2, Question3and4, Question5, SortModule, PrintModule

""" Question 2 dictionaries"""
med_freq_dict = {}
med_category_freq_dict = {}
""" Question 3 and 4 dictionaries"""
individual_med_type_dict = {}
""" Question 5 dictionaries"""
individual_med_dict = {}

def parseFunction():
    with open("medication.csv", newline="", encoding="utf-8") as f:
        """["patient_id", "visit_id", "medication_id", "start", "end", "time", "text", "type1", "type2", "comment"]"""

        reader = list(csv.reader(f))

        # skip the header, hence [1:]
        for row in reader[1:]:

            """ Question 2 code """
            Question2.question2(row, med_freq_dict, med_category_freq_dict)

            """ Question 3 and 4 code """
            Question3and4.question3and4(row, individual_med_type_dict)

            """ Question 5 code """
            Question5.question5(row, individual_med_dict)

            """ Question 6 code """
            # Call to Function here

def main():
    """ change xml to csv if medication.csv doesn't exist """
    xml_to_csv
    
    """ analysis for questions """
    parseFunction()

    """ sort the answers from parseFunction """
    #answers[0] = med_freq_dict, a[1] = med_category_freq_dict, a[2] = individual_med_type_dict, a[3] = individual_med_dict
    answers = SortModule.sortEverything(med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_dict)

    """ print the answers from sortFunction() """
    # a[0] = med_freq_dict, a[1] = med_category_freq_dict, a[2] = individual_med_type_dict, a[3] = individual_med_dict
    PrintModule.printFunction(answers[0], answers[1], answers[2], answers[3])


if __name__ == "__main__":
    main() 