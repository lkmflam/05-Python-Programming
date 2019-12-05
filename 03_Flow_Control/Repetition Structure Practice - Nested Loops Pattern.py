#Starts at 7 as there are 7 rows and 7 stars
row = 7

#As long as the number of rows isn't less than one (impossible) or once the number of rows end, it will print the number of stars specified
#then decrements by one.
while row >= 1:
    if row == 7:
        print("*******")
    elif row == 6:
        print("******")
    elif row == 5:
        print("*****")
    elif row == 4:
        print("****")
    elif row == 3:
        print("***")
    elif row == 2:
        print("**")
    elif row == 1:
        print("*")
    row = row - 1
exit