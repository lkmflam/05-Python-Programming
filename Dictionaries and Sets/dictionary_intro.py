# Dictionaries
# A Dictionary is an object that stores a collection of data. Each element in a dictionary
# has two parts: a key and a value. You use a key to locate a specific value. 

# Creating a dictionary

#phonebook = {'Chris': '555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
# print(phonebook)

# # Retrieving a value from a dictionary
# print(phonebook['Katie'])

# # Using the in and not in operators to test for a value
# if 'Chris' in phonebook:
#     print(phonebook['Chris'])

# if 'David' not in phonebook:
#     print('Not in phonebook')

# # Adding an element to a dictionary
# phonebook['David'] = '555-4444'
# print(phonebook)

# # Remove an element from a dictionary
# del phonebook['David']
# print(phonebook)

# # Finding the length of a dictionary
# length_dictionary = len(phonebook)
# print(length_dictionary)

# # Using update to add items to the dictionary
# print(phonebook)
# phonebook.update({'David': '555-4444', 'Chris':'555-1234'})
# print(phonebook)

# phonebook2 = {'Jim':'123-4567'}
# phonebook.update(phonebook2)
# print(phonebook)

# Different way to write a dictionary
# test_scores = { 'Kayla':[88, 92, 100],
#                 'Luis':[95, 74, 81],
#                 'Sophie':[72, 88, 91],
#                 'Ethan':[70, 75, 78] }
# print(test_scores)

# # Accessing values of different types
# kayla_scores = test_scores['Kayla']
# print(kayla_scores[1])

# # Initialize and empty dictionary
# empty_dictionary = {}
# print(empty_dictionary)
# empty_dictionary[1] = 'This is a value'
# print(empty_dictionary)

# Iterating over a dictionary
# for key in phonebook:
#     print(key)

# for key in phonebook:
#     print(key, phonebook[key])

# The clear method
# dictionary.clear()

# phonebook.clear()
# print(phonebook)

# The get method
# dictionary.get(key, default)
phonebook = {'Chris': '555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
# value = phonebook.get('Katie', 'Entry not found')
# print(value)

# value2 = phonebook.get('David', 'Entry not found')
# print(value2)

# The items method
# print(phonebook.items())

# for key, value in phonebook.items():
#     print(key, value)

# The keys method
# for key in phonebook.keys():
#     print(key)

# for value in phonebook.values():
#     print(value)

# The pop method (removes and returns the key-value pair)
# dictionary.pop(key, default)
phone_num = phonebook.pop('Chris', 'Entry not found')
print(phone_num)
print(phonebook)

phone_num2 = phonebook.pop('Andy', 'Entry not found')
print(phone_num2)
print(phonebook)

# The popitem method
key, value = phonebook.popitem()
print(key, value)

