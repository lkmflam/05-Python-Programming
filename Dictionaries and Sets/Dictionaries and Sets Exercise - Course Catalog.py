def main():
    course_catalog = {'CS101': {'3004', 'Haynes', '8:00 a.m.'},
    'CS102': {'4501', 'Alvarada', '9:00 a.m.'},
    'CS103': {'6755', 'Rich', '10:00 a.m.'},
    'NT110': {'1244', 'Burke', '11:00 a.m.'},
    'CM241': {'1411', 'Lee', '1:00 p.m.' }}
    #print(course_catalog['CS101'])
    print("Welcome to the course catalog system.")
    for coursenumber, course in course_catalog.items():
        print(coursenumber)
    coursenumber =input("Please enter the class for which you wish to view information: ")
    #This is where the problems start. Figure out how to print the information for the specific course number chosen. 
    for coursenumber, course in course_catalog.items():
        print('Course: ', coursenumber)
        for course, information in course_catalog.items():
            print(course_catalog[0])

            #print('guitar sound', instruments['guitar']['sound'])
            course = 0
            information = 0
main()