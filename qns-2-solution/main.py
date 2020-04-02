

# opening a file for 'writing' will overwrite the original file
with open('data.txt', 'w') as fp:
    fruit = input("Enter fruit: ")
    while fruit =='apple' or fruit=='orange' or fruit=='pineapple' or fruit=='watermelon' or fruit=='durian':
        fp.write(fruit+"\n")
        fruit = input("Enter fruit: ")


