#Opens file of names and puts in "write mode"
fileopening = open("names.txt", "w")

#Name is an empty string
name = " "
count = 0

#Has the user enter names until they type "quit". The names are written to the file names.txt. The count for names increases by one with each.
# If the user types "quit" then the loop will be exited. 
while name != "quit":
    name = input("Enter a name: ")
    fileopening.write(name)
    count += 1
print(count)
fileopening.close()

#Reopens the file and reads the names now present within the file
reopen = open("names.txt", "r")
print(reopen.readlines())
reopen.close()