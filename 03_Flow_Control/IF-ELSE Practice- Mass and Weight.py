print("Let's calculate the amount of Newtons an object weighs.")
mass = int(input("Please enter the mass of the object in kilograms."))
weight = mass * 9.8
print("The weight of the object in Newtons is: ", weight)
if weight > 1000:
    print("The object is too heavy.")
elif weight < 10:
    print("The object is too light.")
else:
    pass