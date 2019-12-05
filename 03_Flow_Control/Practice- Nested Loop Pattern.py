row_count = 0
rows_to_print = 7

#Range of 0-7
for row in range(0,rows_to_print):

#Will print the number of stars from 0 to (7- count) so will start at 7 and with each iteration, the count will grow larger
#meaning that the number of stars will grow smaller by one each time
    for row in range(0,rows_to_print - row_count):
        print("*", end = '')
    row_count += 1
    print("")