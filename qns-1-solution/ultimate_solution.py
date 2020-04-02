cost = {}

# parse the costs.txt file to extract fruit name and prices
with open('costs.txt', 'r') as fp:
    for line in fp:
        line = line.strip().lower()
        chunks = line.split("=")

        fruit = chunks[0].strip()
        price = float(chunks[1].strip())
        cost[fruit] = price
        #or:
        #cost[chunks[0].strip()] = float(chunks[1].strip())
        
print(cost)
total = 0

filename = input("Enter filename to read from: ")

with open(filename, 'r') as fp:
    for line in fp:
        fruit = line.strip().lower()
        if fruit in cost: 
            total += cost[fruit]
        else:
            print(fruit,"is not found")

print('total=', total)
