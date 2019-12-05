def main():
    monthly_rainfall= [["January", ""], ["February", ""], ["March", ""], ["April", ""], ["May", ""], ["June", ""], ["July", ""], ["August", ""], ["September", ""], ["October", ""], ["November", ""], ["December", ""]]
    count = 0
    size = len(monthly_rainfall)
    average = 0
    total = 0
    while count < size:
        rainfall = int(input("Please enter the monthly rainfall: "))
        monthly_rainfall[count][1] = rainfall
        average = (rainfall + average) / size
        total = rainfall + total
        count += 1
    print(monthly_rainfall)
    print(total)
    print(average)
main()
