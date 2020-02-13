import csv

def getInformation(cols):
    with open('Informacija/monica.csv', 'rU') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row[cols])
        return data

