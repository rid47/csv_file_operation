import csv


# read as row
with open("test.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(f"content: {', '.join(row)}")
        line_count += 1
    print(f"Total rows: {line_count}")

# read in a dict
with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print(f"using Dictreader: {csv_reader}")
    line_count = 0
    for row in csv_reader:
        print(row)
