|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Lab 2D & Lab2E

**Lab 2D: Strings**

**Instructions:**

Write a program that reverses a user inputted string then outputs the new string, in all uppercase letters.

**Bonus:** Add additional functionality, experiment with other string methods.

main()
user_inputted_string = input("Enter a sentence of your choice for my display. \n")
new_user_string = user_inputted_string[::-1]
print(new_user_string.upper())
Exit()

## Lab 2E: Count Words

**Instructions:**

Write a program that takes a string as user input then counts the number of words in that sentence.

**Bonus:** Add additional functionality, experiment with other string methods.

ex: Output number of characters, number of uppercase letters, etc...

---

main()
user_counting_string = input(Give me a sentence so that I may count the words. \n")
counted_user_string = user_counting_string.split(" ")
print (len(counted_user_string))
Exit()

|[Next Topic](/02_Data_Types/04_lists.md)|
|---|
