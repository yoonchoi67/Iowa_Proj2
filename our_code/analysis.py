import os
from os import listdir
from os.path import isfile, join

print(os.getcwd())
data_path = join(os.getcwd(), "../data")
data_file_list = [join(data_path, f) for f in listdir(data_path)]

print(data_file_list[4])