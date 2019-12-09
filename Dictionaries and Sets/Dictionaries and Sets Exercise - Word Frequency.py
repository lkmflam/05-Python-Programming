opening_file= open("words.txt", "r")
readinglines = opening_file.readlines()
words_dict = {}
for line in readinglines:
    allwords = line.split(" ")
    for word in allwords:
        allwords = word.strip('\n')
        print(allwords)
        #Now that you have a list of the words sorted out, you need to iterate through
        #to see how many times that word has been mentioned and then keep track
        #to be stored in a dictionary.

opening_file.close()
