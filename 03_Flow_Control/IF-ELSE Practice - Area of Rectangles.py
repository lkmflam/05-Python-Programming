print("Let's figure out who the supreme rectangle is. All measurements will be in centimeters. ")
length1 = int(input("Please enter the length of your first rectangle. "))
width1 = int(input("Please enter the width of that same rectangle now. "))
length2 = int(input("Moving on to the second rectangle. Please enter the length. "))
width2 = int(input("Please enter the width for the second rectangle. "))
area1 = (length1 * width1)
print("The area of the first rectangle is ", area1)
area2 = (length2 * width2)
print("The area of the second rectangle is ", area2)
if area1 > area2:
    print("Rectangle one is the largest in area.")
elif area1 == area2:
    print("Ladies and gentlemen, there appears to be a tie.")
else:
    print("Rectangle two is the largest.")