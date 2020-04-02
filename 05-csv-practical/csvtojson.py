import csv
import json
final = []

filename = input("Filename: ")

with open(filename) as fp:
    reader = csv.reader(fp, delimiter=',')

    headers = next(reader)

    for line in reader:
        record = {}
        for index,each_header in enumerate(headers):
            record[each_header] = line[index]
        
        final.append(record)


print(json.dumps(final))