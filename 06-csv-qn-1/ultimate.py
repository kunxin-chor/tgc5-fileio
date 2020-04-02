
# import in the read_librar function from data_processing.py
from data_processing import read_library

def search_book(search):
    search = search.lower().strip()
    wanted_book = library[search]
    return wanted_book

def print_book(book):
    print("Title:", wanted_book['title'])
    print("Author", wanted_book['author'])
    print("ISBN", wanted_book['ISBN'])
    print("Date publshed:", wanted_book['year_published'])

# MAIN #
library = read_library('books.csv')
search = input("Enter title: ")
wanted_book = search_book(search)
print_book(wanted_book)


