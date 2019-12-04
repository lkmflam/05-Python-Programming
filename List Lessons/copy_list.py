# Copying lists in python

# Create a list
list1 = [1, 2, 3, 4]

# assign the list to the list2 variable
list2 = list1

# print the lists
print(list1)
print(list2)

# replace part of the list
list1[0] = 99
print(list1)
print(list2)

# copy of the list that references two separate but
# identical lists

# create a list with values
list3 = [1, 2, 3, 4]

# Create an empty list
list4 = []

print('Original list3', list3)
print('Original list4', list4)

# Copy the elements of list1 to list2
for item in list3:
    list4.append(item)

print('After append list3', list3)
print('After append list4', list4)

# replace part of the list
list3[0] = 99
print(list3)
print(list4)


