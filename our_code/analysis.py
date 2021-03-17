import os
from os import listdir
from os.path import join
import pandas as pd
import xml.etree.ElementTree as ET

# print(os.getcwd())
path = join(os.getcwd(), "../data")
files = [join(path, f) for f in listdir(path)]

column_names = ["patient_id", "visit_id", "medication_id", "start", "end", "time", "text", "type1", "type2", "comment"]
med_df = pd.DataFrame(columns=column_names)

def extract(f):
    tree = ET.parse(f)
    root = tree.getroot()
    
    file_name = os.path.split(f)[1]
    file_name = file_name.split("-")
    patient_id = file_name[0]
    visit_id = file_name[1].split(".")[0]
    
    print("patient ID", patient_id)
    for each in root.iter("MEDICATION"):
        med_df.loc[len(med_df)] = [
            patient_id, 
            visit_id, 
            each.get('id'), 
            each.get('start'), 
            each.get('end'), 
            each.get('time'), 
            each.get('text'), 
            each.get('type1'), 
            each.get('type2'), 
            each.get('comment')
            ]
    
[extract(f) for f in files]
med_df.to_csv("medication.csv", index=False)