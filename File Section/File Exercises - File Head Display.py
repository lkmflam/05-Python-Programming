#Reads lines from the file and prints the first five lines 


#Opens the user's file as read-only and set to variable
fileopen = open(input("Please enter the name of the file that you wish to open."), 'r')

#Reads multiple lines and sets that equal to variable
lines = fileopen.readlines()

#Count the number of lines in the file and then sets that number to a variable
#So count will equal the length of the file
count = len(lines)

#If the line count is greater than the specified range of 5 lines, only the first 5 lines will be printed.
for num in range(0,4):
    if num < count:
        print(lines[num])

#Closes the file
fileopen.close()