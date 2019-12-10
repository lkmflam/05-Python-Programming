opening_file= open("words.txt", "r")
readinglines = opening_file.readlines()
words_dict = {}
#This section prepares each line in the file to broke down. It strips out the spaces and \n
#Then it splits the words on the spaces so it knows how far the string extends
for line in readinglines:
    line = line.strip()
    line = line.split(" ")
    print(line)
#States that if the words from the line are already present in the dictionary made, it will add a 1 to the count to be referenced later
    for word in line:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    print(word)
    print(words_dict)
#Now that we have our dictionary set up, we will print the key(the word) and the associated number.
for key in list(words_dict.keys()):
    print(key, ":", words_dict[key])
opening_file.close()
