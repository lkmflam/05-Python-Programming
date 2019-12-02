door_number = input("Welcome to the Fun House! Choose door 1, 2, or 3...")

print(door_number)

if door_number == "1":
    print("Ahh the safe option? You bore me. That was the exit door.")
    exit
elif door_number == "2":
    print("Enter at your own risk. You have come upon another two doors? Choose 1 or 2.")
    if door_number == "1":
        print("Thanks for playing in my Fun House. You have chosen the exit door.")
    elif door_number == "2":
        print("Death becomes you. Oh what fun!")
    else:
        print("You defy me and the options that I have given you.")
        exit
elif door_number == '3':
    print("Door 3? Ahh, you enjoy risky business! Collect your $100 before exiting.")
else:
    print("That was not one of the options. Leave this house.")
    exit
