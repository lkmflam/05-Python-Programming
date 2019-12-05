print("Let's find out how many calories were burned while running")
calories = 0

#Starts at 10, 15, 20, 25, 30.
minutes = 10

#As long as the time does not exceed 30 minutes, it will multiply the calories by minute and print the amount at the time.
while minutes <= 30:
    calories = 3.9 * minutes
    message = "The number of calories burned at {} minutes is: {}".format(minutes, calories)
    print(message)

#Adds 5 to the count of minutes to increment by the value
    minutes = minutes + 5
exit