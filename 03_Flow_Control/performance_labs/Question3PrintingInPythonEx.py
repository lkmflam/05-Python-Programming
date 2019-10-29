main()
    feetperacre = 43560
    totalsquarefeet = input("Please enter the total square feet in the tract of land.")
    acre = totalsquarefeet / feetperacre
    acreageinfo = {'feet': feetperacre, 'total': totalsquarefeet, 'total acres': acre}
    print("There are {feet} feet in an acre. You input that your tract is {total} square feet large.
    With this information, your tract is {total acres} acres large.") 
end()

