print("Let's collect some bugs!")
daycount = 0
totalbug = 0
while daycount < 8:
    numbug = int(input("Please enter the number of bugs for the day."))
    totalbug = totalbug + numbug
    daycount = daycount + 1
print("The total number of bugs collected over the week is:",totalbug)