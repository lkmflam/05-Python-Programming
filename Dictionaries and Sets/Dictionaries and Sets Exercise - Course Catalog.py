def main():
    course_catalog = {'CS101': ['3004', 'Haynes', '8:00 a.m.'],
    'CS102': ['4501', 'Alvarada', '9:00 a.m.'],
    'CS103': ['6755', 'Rich', '10:00 a.m.'],
    'NT110': ['1244', 'Burke', '11:00 a.m.'],
    'CM241': ['1411', 'Lee', '1:00 p.m.' ]}
    print("Welcome to the course catalog system.")
    #Stores the course number and the asscoiated data will be named course and prints the numbers.
    for coursenumber, course in course_catalog.items():
        print(coursenumber)
    coursenumber = input("Please enter the class for which you wish to view information: ")
    #If the course number doesn't equal the course numbers available, continues to ask user for valid course
    while coursenumber != "CS101" and coursenumber != "CS102" and coursenumber != "CS103" and coursenumber != "NT110" and coursenumber != "CM241":
        coursenumber = input("Sorry, but that course is not available in the course catalog. Please enter a valid course. ")
    print(coursenumber)
    print("Time: ",course[2])
    print("Instructor: ", course[1])
    print("Room Number: ", course[0])
main()