import os
from os import listdir
from os.path import join
import pandas as pd
import pandas as pd
import numpy as np
from collections import defaultdict 

def csvFunction(med_freq_dict, med_category_freq_dict, individual_med_type_dict, individual_med_type_count_dict, individual_med_dict):
    
    path = join(os.getcwd(), "../analysis_data2")
    if not os.path.exists(path):
        os.makedirs(path)

    """ Write to csv for question 2 (medicine frequency distribution) """
    column_names = ["med", "frequency"]
    med_df = pd.DataFrame(columns=column_names)
    if not os.path.exists(join(path, 'med_freq_dist(q2).csv')):
        med_freq_dict = dict(med_freq_dict)
        for k, v in med_freq_dict.items():
            med_df.loc[len(med_df)] = [k, v]
        if not os.path.exists(join(path, 'med_freq_dist(q2).csv')):
            med_df.to_csv(join(path, 'med_freq_dist(q2).csv'), index=False)
    
    """ Write to csv for question 2 (categories of medicine frequency distribution) """
    column_names = ["med_category", "frequency"]
    med_df = pd.DataFrame(columns=column_names)    
    if not os.path.exists(join(path, 'categ_med_freq_dist(q2).csv')):
        med_category_freq_dict = dict(med_category_freq_dict)
        for k, v in med_category_freq_dict.items():
            med_df.loc[len(med_df)] = [k, v]
        if not os.path.exists(join(path, 'med_category_freq_dict(q2).csv')):
            med_df.to_csv(join(path, 'med_category_freq_dict(q2).csv'), index=False)

    """ Write to csv for question 3 and 4 """
    column_names = ["patient_id", "num of medication types"]
    med_df = pd.DataFrame(columns=column_names)
    if not os.path.exists(join(path, 'individual_med_type_dict(q3&4).csv')):
        individual_med_type_dict = dict(individual_med_type_dict)
        for k, v in individual_med_type_dict.items():
            med_df.loc[len(med_df)] = [k, v]
        if not os.path.exists(join(path, 'individual_med_type_dict(q3&4).csv')):
            med_df.to_csv(join(path, 'individual_med_type_dict(q3&4).csv'), index=False)

    """ Write to csv for question 5 """
    column_names = ["patient_id", "num of medication"]
    med_df = pd.DataFrame(columns=column_names)
    if not os.path.exists(join(path, 'individual_med_dict(q5).csv')):
        individual_med_dict = dict(individual_med_dict)
        for k, v in individual_med_dict.items():
            med_df.loc[len(med_df)] = [k, v]
        if not os.path.exists(join(path, 'individual_med_dict(q5).csv')):
            med_df.to_csv(join(path, 'individual_med_dict(q5).csv'), index=False)
