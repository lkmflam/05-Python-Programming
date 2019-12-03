row_count = 0
rows_to_print = 7
for row in range(0,rows_to_print):
    for row in range(0,rows_to_print - row_count):
        print("*", end = '')
    row_count += 1
    print("")