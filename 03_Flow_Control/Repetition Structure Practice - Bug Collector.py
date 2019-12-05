print("Let's collect some bugs!")
daycount = 0
totalbug = 0

#Less than 7 days since te index values are 0-6 =7.
#Will continuously ask user to enter the number of bugs for each day until the count reaches 7 which is past the week mark.
while daycount < 7:
    numbug = int(input("Please enter the number of bugs for the day."))
    totalbug = totalbug + numbug
    daycount = daycount + 1

#Prints the number of bugs
print("The total number of bugs collected over the week is:",totalbug)