import csv

def import_dream_data(path):
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        previous = 0
        for row in reader:
            for trades in range(int(row[0])):
                data.append(int(row[1]) + previous)
            previous = data[-1]
    return data
