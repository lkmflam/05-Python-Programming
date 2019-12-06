#Rainfall Statistics
#Design a program that lets the user enter the total rainfall for each of 12 months into a list.
#The program should calculate and display the total rainfall for the year, the average monthly
#rainfall, and the months with the highest and lowest amounts.

def main():
    #Ask user input for the month and the rainfall
    monthly_rainfall= [["January", ""], ["February", ""], ["March", ""], ["April", ""], ["May", ""], ["June", ""], ["July", ""], ["August", ""], ["September", ""], ["October", ""], ["November", ""], ["December", ""]]
    count = 0
    size = len(monthly_rainfall)
    average = 0
    total = 0
    while count < size:
#For each month (the count will start at 0 and increment throughout the size of 12 since there are 12 months)
        rainfall = int(input("Please enter the monthly rainfall: "))
#The user will enter the rainfall amount and it will be coonverted to an integer so that it can be used in math later.
        monthly_rainfall[count][1] = rainfall
#The rainfall amount for the month will be stored in the empty quotes for that month.
        average = (rainfall + average) / size
        total = rainfall + total
        count += 1
    print(monthly_rainfall)
    print(total)
    print(average)
#Above is the math to be able to find the total and average amount of rainfall.
main()
