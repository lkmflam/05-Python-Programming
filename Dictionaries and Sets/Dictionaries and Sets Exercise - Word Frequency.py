opening_file= open("words.txt", "r")
readinglines = opening_file.readlines()
words_dict = {}
for line in readinglines:
    allwords = line.split(" ")
    for word in allwords:
        word = word.strip('\n')
        print(word)
        
opening_file.close()
