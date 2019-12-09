opening_file= open("words.txt", "r")
readinglines = opening_file.readlines()
#print(readinglines)
unique_word_set = set()
words_list= []
for line in readinglines:
    words_list = line.split(" ")
    for word in words_list:
        word = word.strip('\n')
        unique_word_set.add(word)
print(unique_word_set)
opening_file.close()

'''.split() is a method of a string that creates a list from a deliminated string
so if you .split(" ") on a sentence, it'll give you each word
in a list
iterate through the list of words and add each one to the set
readlines() automatically gives you a list of the lines in a file'''

'''> open a file
> read the lines of the file
> create a set
> enter a loop
> for each line of content
     > split line into list of words
> loop through list of words
> add each word to the set (because the add() method does not allow for duplicates
> print the set'''