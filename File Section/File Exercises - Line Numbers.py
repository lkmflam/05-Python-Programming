#Opens the file that the user specifies
fileopen = open(input("Please enter the name of the file that you wish to open."), 'r')

#Reads the lines within the file and determines the length of the file
lines = fileopen.readlines()
count = len(lines)

#Count is how long the file is, so number is the index values basically.
#As long as the number variable is less than the amount of lines in the file (because one must be subtracted since the index starts at 0) the 
#number will be printed in front of the lines found in the file.
number = 0
while number < count:
    print(number,".",lines[number])
    number = number + 1
fileopen.close()