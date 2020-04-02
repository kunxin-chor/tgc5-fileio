with open('data.txt', 'r') as fp:
    total = 0
    for line in fp:
        # print(line.strip())  # be careful -- anything methods called on a string does not change it
                             # strings are immutable.
        line = line.strip()  # must reassign the result of the strip method back to the variable itself for it to be permanet
        line = line.lower()  # convert to lower case for ease of comparison
        if line=='apple':
            total += 0.5
        if line=='orange':
            total +=0.7
        if line=='pineapple':
            total += 1
        if line=='watermelon':
            total +=2.5
        if line=='durian':
            total+=10
        if line=='banana':
            total+=0.25

print("Total=", total)