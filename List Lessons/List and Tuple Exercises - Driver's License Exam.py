def main():
    answer_sheet = [[1, 'B'], [2, 'D'], [3, 'A'], [4, 'A'], [5, 'C'], [6, 'A'], [7, 'B'], [8, 'A'], [9, 'C'], [10, 'D'], [11, 'B'], 
    [12, 'C'], [13, 'D'], [14, 'A'], [15, 'A'], [16, 'C'], [17, 'C'], [18, 'B'], [19, 'D'], [20, 'A']]
    print(answer_sheet[1][1])
    student_sheet = [[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, ''], [10, ''], [11, ''], [12, ''],
    [13, ''], [14, ''], [15, ''], [16, ''], [17, ''], [18, ''], [19, ''], [20, '']]
    count = 0
    testlength= len(answer_sheet)
    print("You will begin your driver's exam. Good luck and no cheating acceptable.")
    while count < testlength:
        number = str(count + 1)
        #Come back and fix print and input statements because it is not accepting the input
        answerquestion = print("Answer",number,":")
        answer = input(answerquestion) 
        print(answer)
        answer_sheet[count][1] = answer
        print(answer_sheet)
        #Only here as a place holder
        print(student_sheet)

main()