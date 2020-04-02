cost = {
    'apple':0.5,
    'orange':0.7,
    'pineapple':1,
    'watermelon':2.5,
    'durian':10,
    'banana':0.5
}

total = 0

with open('data2.txt', 'r') as fp:
    for line in fp:
        fruit = line.strip().lower()
        if fruit in cost: 
            total += cost[fruit]
        else:
            print(fruit,"is not found")

print('total=', total)
