import csv


csvfile = open('../../data/chp3/data-text.csv', 'rb')
# reader = csv.reader(csvfile)
reader = csv.DictReader(csvfile)

for row in reader:
    print row
