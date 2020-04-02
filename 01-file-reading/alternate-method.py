#open the file and set the fil epointer into the filepointer variable
with open('data.txt', 'r') as filepointer:  #with block
    for line in filepointer:
        print(line.strip())

#there is no need to close
