import csv

costs = {}

with open('cost.csv', 'r') as fp:
    reader = csv.reader(fp,delimiter=",") #we create the csv reader from the file pointer

    #read in the rest of the file
    for line in reader:
        fruit = line[0]
        price = float(line[1])
        costs[fruit] = price

print(costs)
print(costs['apple'])