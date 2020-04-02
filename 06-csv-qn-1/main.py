import csv

def extract_book(array):
    return {
        'ISBN':array[0],
        'title':array[1],
        'author':array[2],
        'year_published':array[3]
    }


library = {}
with open('books.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',')
    headers = next(reader)

    for line in reader:
        #line will be a list of the row
        book = extract_book(line)
        title = book['title']
        library[title.lower()] = book
        # library[book['title']] = book

search = input("Enter title: ")
search = search.lower().strip()
wanted_book = library[search]
print("Title:", wanted_book['title'])
print("Author", wanted_book['author'])
print("ISBN", wanted_book['ISBN'])
print("Date publshed:",wanted_book['year_published'])

        
