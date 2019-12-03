budget = int(input("Please enter your budget for the month: "))
print("You will be asked to continuously add to your list of expenses. \
When finished, please press  '0' when prompted.")
expenses = 0
newexpense = 1
while newexpense > 0:
    newexpense = int(input("Please enter an expense: "))
    expenses = expenses + newexpense
limit = expenses - budget
if limit > 0:
    print("You went over budget this month by: $ ", limit)
else:
    print("You were under budget this month by: $ ", limit)
exit