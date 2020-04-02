filename = input("Enter the filename to save to: ")

valid_fruits = ['apple','orange','pineapple', 'watermelon', 'durian']

# opening a file for 'writing' will overwrite the original file
with open(filename, 'w') as fp:
    fruit = input("Enter fruit: ")
    fruit = fruit.strip().lower()
    while fruit in valid_fruits:
        fp.write(fruit+"\n")
        fruit = input("Enter fruit: ")


