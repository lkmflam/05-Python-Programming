#The local driver’s license office has asked you to create an application that grades the written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
#are the correct answers:
#1. B    6. A    11. B   16. C
#2. D    7. B    12. C   17. C
#3. A    8. A    13. D   18. B
#4. A    9. C    14. A   19. D
#5. C    10. D   15. D   20. A
#Your program should store these correct answers in a list. The program should read the
#student’s answers for each of the 20 questions from a text file and store the answers in
#another list. (Create your own text file to test the application.) After the student’s answers
#have been read from the file, the program should display a message indicating whether the
#student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
#to pass the exam.) It should then display the total number of correctly answered questions,
#the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.

def main():
    answer_sheet = [[1, 'B'], [2, 'D'], [3, 'A'], [4, 'A'], [5, 'C'], [6, 'A'], [7, 'B'], [8, 'A'], [9, 'C'], [10, 'D'], [11, 'B'], 
    [12, 'C'], [13, 'D'], [14, 'A'], [15, 'A'], [16, 'C'], [17, 'C'], [18, 'B'], [19, 'D'], [20, 'A']]
    student_sheet = [[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, ''], [10, ''], [11, ''], [12, ''],
    [13, ''], [14, ''], [15, ''], [16, ''], [17, ''], [18, ''], [19, ''], [20, '']]
    count = 0
    testcount = 0
    testlength= len(answer_sheet)
    answercount = 0
    print("You will begin your driver's exam. Good luck and no cheating acceptable.")
    while count < testlength:
        number = str(count + 1)
        print("Answer",number,":", end = ' ')
        while True:
            answer = input()
            if answer.lower() not in ('a', 'b', 'c', 'd'):
                print("Not an appropriate choice. Please input the correct letter.")
            else: break
        student_sheet[count][1] = answer.upper()
        count += 1
#Will store the answer in the number of the index, the same as the question and in upper case for easier reference.
#Also does error handling so it will ask the user to try again if not an allowed answer in either upper or lower case.
    while testcount < testlength:
        if answer_sheet[testcount][1] == student_sheet[testcount][1]:
            answercount +=1
        else:
            answercount = answercount + 0
        testcount += 1
    passdifference = testlength - answercount
#Above will test whether or not the answer value matches from the student and the answer key. 
#If it does, it will add to the number of correct answers. This repeats for the length of the test questions.
#Finally, the number of correct answers is subtracted from the number of questions for the difference. 
    if passdifference == 0:
        print(passdifference, "Congratulations you got 100% of the questions right")
    else:
        if passdifference < 6:
            print("Congratulations, you have passed! Your score is:",answercount,"/20", end = '')
        else:
            print("You have failed the exam. Your score is:",answercount,"/20", end = '')
main()
#The difference number above is used to measure whether or not the student passed or failed. If the difference is less than 6, this means that
#the student would have gotten a 15 or higher and it prints that they passed and what the score was. Same if they failed.