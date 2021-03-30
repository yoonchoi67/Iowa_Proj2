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

    for i, each in enumerate(root.iter("MEDICATION")):        
        text=''
        type1=''
        type2=''
        comment=''
        if each.get('text') is not None: text = each.get('text').lower().strip()
        else: text = None

        if each.get('type1') is not None: type1 = each.get('type1').lower().strip()
        else: type1 = None

        if each.get('type2') is not None: type2 = each.get('type2').lower().strip() 
        else: type2 = None

        if each.get('comment') is not None: comment = each.get('comment').lower().strip() 
        else: comment = None

        med_df.loc[len(med_df)] = [
            patient_id, 
            visit_id, 
            each.get('id'), 
            each.get('start'), 
            each.get('end'), 
            each.get('time'), 
            text, 
            type1, 
            type2, 
            comment
            ]
    
        
    
""" Create a medication.csv if not exists already """
if not os.path.exists('medication.csv'):
    [extract(f) for f in files]
    med_df.to_csv("medication.csv", index=False)



d = dict()
m_count = 0
none_count = 0
doc_count = 0
all_count = 0

def extract2(f):
    global d, m_count, none_count, doc_count, all_count
    tree = ET.parse(f)
    root = tree.getroot()
    for i, elem in enumerate(root.iter()):
        all_count += 1   
        if type(elem.get('id')) == type(None): 
            # print(type(elem.get('id')))
            none_count += 1       
            continue
        if 'M' in elem.get('id'): 
            m_count += 1
            continue
        if 'DOC' in elem.get('id'):
            doc_count += 1
            # continue
            if elem.tag not in d: d[elem.tag] = 1
            else: d[elem.tag] += 1
        

[extract2(f) for f in files]

added_all_count = none_count+m_count+doc_count

print("All count: ", all_count)
print("added_all_count", added_all_count)
print(d)