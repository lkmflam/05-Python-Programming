fileopen = open(input("Please enter the name of the file that you wish to open."), 'r')
lines = fileopen.readlines()
count = len(lines)
number = 0
while number < count:
    print(number,".",lines[number])
    number = number + 1
fileopen.close()