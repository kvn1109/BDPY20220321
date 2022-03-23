import csv

csv_file_path = "data/data54.csv"

csvFile1 = open(csv_file_path)
reader1 = csv.reader(csvFile1)
sampleData = list(reader1)

csvFile1.close()

print(type(sampleData))
for row in sampleData:
    print(row)
    for col in row:
        print(col)