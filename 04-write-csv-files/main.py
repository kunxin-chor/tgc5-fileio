import csv

filename = "info.txt"
with open(filename, 'w') as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(["Avengers", "2015"])
    writer.writerow(["Lord of the Rings", "1999"])
    writer.writerow(["Parasite", "2019"])
    writer.writerow(["I, Robot", "2008"])


