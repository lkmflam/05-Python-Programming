fileopen = open(input("Please enter the name of the file that you wish to open."), 'r')
lines = fileopen.readlines()
count = len(lines)
for num in range(0,4):
    if num < count:
        print(lines[num])
fileopen.close()