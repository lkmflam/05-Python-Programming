# Sets
# A set contains a collection of unique values
# and works like a mathematical set

# 1. All the elements in a set must be unique. no
# two elements can have the same value

# 2. Sets are unordered, which means that the 
# elements are not stored in any particular order

# 3. The elements that are stored ina set can be of
# different data types.

# Creating a set
# my_set = set(['a', 'b', 'c'])
# print(my_set)

# my_set2 = set('abc')
# print(my_set2)

# my_set3 = set('aabbcc')
# print(my_set3)

my_set4 = set('one two three')
print(my_set4)

# find length of the set
print(len(my_set4))

# adding and removing elements of a set
new_set = set()
new_set.add(1)
new_set.add(2)
new_set.add(3)
print('new_set', new_set)

new_set.update([4,5,6])
print('after update', new_set)

new_set2 = ([7,8,9])
new_set.update(new_set2)
print('after variable update', new_set)

new_set.remove(1)
print(new_set)

# keyerror
# new_set.remove(10)

# using discard
new_set.discard(10)
print(new_set)

# using for loop to iterate over a set
new_set3 = set(['a','b','c'])
for val in new_set3:
    print(val)

# Using in and not in operators to test a value in the set
numbers_set = ([1, 2, 3])
if 1 in numbers_set:
    print('The value 1 is in the set')

if 99 not in numbers_set:
    print('The value 99 is not in the set')

# Find the union of sets
set1 = set([1, 2 ,3 ,4])
set2 = set([3, 4, 5, 6])
set3 = set1.union(set2)
print('set1', set1)
print('set2', set2)
print('set3', set3)

set5 = set1 | set2
print('set5', set5)

# Find the intersection of sets
set4 = set1.intersection(set2)
print('set4',set4)

set6 = set1 & set2
print('set6', set6)

char_set = set(['abc'])
char_set_upper = set(['ABC'])
char_intersect = char_set.intersection(char_set_upper)
print('char_intersect', char_intersect)

char_union = char_set.union(char_set_upper)
print('char_union', char_union)

# Find the difference of sets
set7 = set1.difference(set2)
set8 = set2.difference(set1)
print('set7',set7)
print('set8',set8)

set9 = set1 - set2
print('set9', set9)

# Finding symmetric difference of sets
set10 = set1.symmetric_difference(set2)
print('set10', set10)

set11 = set1 ^ set2
print('set11', set11)

# Finding subsets and supersets
set12 = set([1,2,3,4,])
set13 = set([1,2])
print(set13.issubset(set12))
print(set12.issuperset(set13))





