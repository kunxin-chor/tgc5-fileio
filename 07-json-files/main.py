import json

with open('transactions.json', 'r') as fp:
    data = json.load(fp)
    print(data)