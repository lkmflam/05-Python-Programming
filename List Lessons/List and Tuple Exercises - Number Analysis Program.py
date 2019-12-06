#4. Number Analysis Program
#Design a program that asks the user to enter a series of 20 numbers. The program should
#store the numbers in a list and then display the following data:
#• The lowest number in the list
#• The highest number in the list
#• The total of the numbers in the list
#• The average of the numbers in the list

def main():
    twenty_numbers = []
    count = 0
    total = 0 
    average = 0
    list_length = 20
    while count < list_length:
        number = int(input("Please enter a number of your choice: "))
        twenty_numbers.append(number)
        total = total + number
        count += 1
    average = total / list_length
    maximum = max(twenty_numbers)
    minimum = min(twenty_numbers)
#Or you could write is as 
# print("Maximum element in the list is :", max(lst), 
# "\nMinimum element in the list is :", min(lst))
    print("Average: ",average,"\nTotal: ",total,"\nMaximum: ",maximum,"\nMinimum: ",minimum)
main()