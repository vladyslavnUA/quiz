import os
import signal

#all wrong answers
answers = []
#all correct answers
canswers = []

print("Welcome to the Capital City Quiz! Here, you will be asked a series of "
"questions about various capital cities in the world.")

def begin():
    #let's ask the user whether they want to play or not
    please = input('do you want to try the quiz? type ye or no: ')

    if please == 'ye' or please == 'y':
        print('[resume ...]')
        print('\n')
        questions()
    else:
        print('goodbye.')
        #ends the program, user didn't want to play :(
        os.kill(os.getpid(),signal.SIGKILL)

def questions():
    score = 0
    print('multiple choice. enter letters from a-e.')
    q1 = input('1. what is the capital city of belgium?\n a. mexico city\n b. ottawa'
               '\n c. brussels\n d. washington d.c.\n e. bangkok\n > ')
    if q1 == 'c':
        print('\n')
        print('good job, belgium would be proud')
        canswers.append('question 1: correct')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('\n')
        print('nope, the answer is brussels')
        answers.append('question 1: wrong')
        print('\n')

    q2 = input('2. what is the capital city of venezuela?\n a. cardiff\n b. buenos aires'
               '\n c. cairo\n d. dublin\n e. caracas\n > ')
    if q2 == 'e':
        print('\n')
        print('good job, that\'s right')
        canswers.append('question 2: correct')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('\n')
        print('nope, the answer is caracas')
        answers.append('question 2: wrong')
        print('\n')

    q3 = input('3. how many capital cities does malaysia have?\n > ')
    val1 = int(q3)
    if val1 == 13:
        print('\n')
        print('good job, that\'s correct.')
        canswers.append('question 3: correct')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('\n')
        print('nope, the answer is 13')
        answers.append('question 3: wrong')
        print('\n')

    q4 = input('4. how many capital cities does bolivia have?\n > ')
    val2 = int(q4)
    if val2 == 2:
        print('\n')
        print('good job, that\'s correct.')
        canswers.append('question 4: correct')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('\n')
        print('nope, the answer is 2')
        answers.append('question 4: wrong')
        print('\n')

    q5 = input('5. true or false: venice is sinking at the rate of 1-2 millimeters a year.\n'
               'enter 1 for true // 0 for false: ')
    val3 = int(q5)
    if q5 == '1':
        print('\n')
        print('that is correct. how\'d you know?')
        canswers.append('question 5: correct')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('\n')
        print('nope, that is true')
        answers.append('question 5: wrong')
        print('\n')

    q6 = input('6. true or false: The canal generates fully one-third of panama’s entire economy.\n'
               'enter 1 for true // 0 for false: ')
    val4 = int(q6)
    if q6 == '1':
        print('\n')
        print('that is correct')
        canswers.append('question 6: correct')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('\n')
        print('nope, that is true')
        answers.append('question 6: wrong')
        print('\n')

    print(f'your correct answers list: {canswers}')
    print('\n')
    print(f'your incorrect answers list: {answers}')
    print('\n')
    print(f'your total score: {score} / 6\n')
    again()
        
def again():
    que = input('would you like to try again? type y or n\n > ')
    if que == 'y':
        begin()
    else:
        os.kill(os.getpid(),signal.SIGKILL)
    
begin()
