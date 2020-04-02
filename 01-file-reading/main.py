filepointer = open('./data.txt', 'r')
for line in filepointer:
    print(line.strip())

filepointer.close() #when program using a file, have to close it, or else may cause problems later on

