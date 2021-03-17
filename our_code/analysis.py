import csv

with open("medication.csv", newline="", encoding="utf-8") as f:
    reader = list(csv.reader(f))
    for row in reader[:10]:
        print(row)    