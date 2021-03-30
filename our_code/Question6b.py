
import os
from os import listdir
from os.path import join
import pandas as pd
import xml.etree.ElementTree as ET

path = join(os.getcwd(), "../data")
files = [join(path, f) for f in listdir(path)]

d = dict()
m_count = 0
none_count = 0
doc_count = 0
all_count = 0

def extract(f):
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
        
def question6b():
    [extract(f) for f in files]

    added_all_count = none_count+m_count+doc_count
    print("DOC COUNT: ", doc_count)
    print("All count: ", all_count)
    print("added_all_count", added_all_count)
    print(d)