#Creates an empty list for the store sales and sets the count so that it will stop requesting input at the end of the week.
def main():
    storesales = []
    day = 7
    count = 0
#As long as the count is less than (0-6) then it will repreatedly ask for input of the store sales for each day of the week
#Then the sales will be added to the list. Specifically added to the end.
    while count < day:
        sale = float(input("Please enter the sales amount for the day: "))
        storesales.append(sale)
        count += 1
#The list will be printed and the total which is the amount stored in each index value and added together. 
#The total is gathered from another function below.
    print(storesales)
    print("The total is: $", get_total(storesales))
#Function to get the total is employed for the list. The total starts at 0 and then for each number in the list, it adds to the total
#and returns it so that it can be invoked in the main function above where it will be used to print.
def get_total(storesales):
    total = 0
    for num in storesales:
        total += num
    return total
main()