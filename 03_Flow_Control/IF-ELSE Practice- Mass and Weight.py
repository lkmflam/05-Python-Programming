#Takes user input for the mass and converts the string to an integer so that it can be used to calculate the weight.
print("Let's calculate the amount of Newtons an object weighs.")
mass = int(input("Please enter the mass of the object in kilograms."))
weight = mass * 9.8

#Prints the weight and then if it's larger than 1000, prints too large or less than 10 and it's too light.
print("The weight of the object in Newtons is: ", weight)
if weight > 1000:
    print("The object is too heavy.")
elif weight < 10:
    print("The object is too light.")
else:
    pass