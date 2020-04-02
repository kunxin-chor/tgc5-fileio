# file writing demo

# 1. open a file for reading
fp = open('data.txt', 'w')  # the second argument 'w' means write to a file
                            # if the file we are writing to does not exist, it will create a new one
                            # if the file exists, then we will OVERWRITE it

#2. use the write method to write to a file
fp.write("You are my sunshine\n")  #we have to put it the \n ourselves
fp.write("my only sunshine\n")
fp.write("you make me happy when the virus is around")

#3 close the file
fp.close()