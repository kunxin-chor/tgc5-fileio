with open('countries.txt', 'a') as fp:  #the 'a' means append
    
    country = input("Please enter a country: ")
    while country != "":
        fp.write(country+'\n')
        country = input("Please enter a country: ")

