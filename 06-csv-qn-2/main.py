import csv

with open('books.csv', 'a') as fp:
    
    writer = csv.writer(fp, delimiter=',')
    
    add_book = input("Add new book? (y/n)")
    while add_book == 'y':
        title = input("title: ")
        author = input("author: ")
        isbn = input('isbn: ')
        year_published = input('year published: ')
        writer.writerow([title, author, isbn, year_published])
        add_book = input("Add new book? (y/n) ")
        
