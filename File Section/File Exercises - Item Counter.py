fileopening = open("names.txt", "w")
name = " "
count = 0
while name != "quit":
    name = input("Enter a name: ")
    fileopening.write(name)
    count += 1
print(count)
fileopening.close()
reopen = open("names.txt", "r")
print(reopen.readlines())