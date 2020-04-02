import json

students = []  #this list is to hold all the students

keep_adding = input("Keep adding students? (y/n) ")

# if the user type in anything that beings with lower case 'y', we take it as 'yes'
while keep_adding.strip().lower()[0] == 'y':
    fname = input('first name: ')
    lname = input('last name: ')
    year = int(input('year: '))

    new_student = {
        'firstname': fname,
        'lastname': lname,
        'year': year
    }

    students.append(new_student)
    keep_adding = input("Keep adding students? (y/n) ")

with open('students.json', 'w') as fp:
    json.dump(students, fp)
