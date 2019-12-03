print("Let's find out how many calories were burned while running")
calories = 0
minutes = 10
while minutes <= 30:
    calories = 3.9 * minutes
    message = "The number of calories burned at {} minutes is: {}".format(minutes, calories)
    print(message)
    minutes = minutes + 5
exit