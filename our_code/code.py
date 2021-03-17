import csv

with open('medication.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)    