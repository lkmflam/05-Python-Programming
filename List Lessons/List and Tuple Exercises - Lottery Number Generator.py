#Create a blank list and state that for a range of 7 numbers, I want each number to be between 0 and 9 (randomly) and then
#be appended to the list. Afterward, the list will be printed.
#Note: It only works when I finally called main at the bottom. I defined main at the top but it needs to be called to execute.
def main():
    lottery_number = []
    import random
    for number in range(7):
        number = random.randint(0,9)
        lottery_number.append(number)
    print(lottery_number)
main()


