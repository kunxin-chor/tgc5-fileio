import csv

with open('data.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=",") #delimiter is optional, it represents the character that seperates the data point
   
    #skip one line
    next(reader)

    for line in reader:
        #print(line) #each line is actually one row from the csv file, in a list/array format
        print("Name:",line[0])
        print("Address:",line[1])
        print("Salary:",line[2])
        print()