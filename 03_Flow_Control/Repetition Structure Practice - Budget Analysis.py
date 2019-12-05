#Requests budget amount from user
budget = int(input("Please enter your budget for the month: "))
print("You will be asked to continuously add to your list of expenses. \
When finished, please press  '0' when prompted.")

#Expenses start at 0 as nothing is entered yet and newexpense is set to 1 so that the sentinel can be 0 and allow the user to ecape
#and to stop adding expenses (new expense will change after this point so the starting amount doesn't matter)
expenses = 0
newexpense = 1

#As long as the user doesn't escape with the 0, they will be asked to enter new expenses which will be added to the
#running total. Then the budget is subtracted from the expenses. If the limit is is positive then they went over, if negative then they stayed
#under budget.
while newexpense > 0:
    newexpense = int(input("Please enter an expense: "))
    expenses = expenses + newexpense
limit = expenses - budget

#Like above, if the limit is postive, then the user is over budget, which will be displayed along with by how much.
if limit > 0:
    print("You went over budget this month by: $ ", limit)
else:
    print("You were under budget this month by: $ ", limit)
exit