import csv

def read_library(filename):
    library = {}
    with open(filename, 'r') as fp:
        reader = csv.reader(fp, delimiter=',')
        headers = next(reader)

        for line in reader:
            # line will be a list of the row
            book = extract_book(line)
            title = book['title']
            library[title.lower()] = book
            # library[book['title']] = book
    return library


def extract_book(array):
    return {
        'ISBN': array[0],
        'title': array[1],
        'author': array[2],
        'year_published': array[3]
    }

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


