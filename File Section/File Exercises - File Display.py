#Opens file (read only), reads it, and prints out the contents before closing
file = open("numbers.txt", 'r')
contents = file.read()
print(contents)
file.close()