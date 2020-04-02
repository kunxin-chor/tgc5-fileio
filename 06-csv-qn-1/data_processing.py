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
