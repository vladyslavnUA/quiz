import os
import signal

print("Welcome to the Capital City Quiz! Here, you will be asked a series of "
"questions about various capital cities in the world.")

def begin():
    #let's ask the user whether they want to play or not
    please = input('do you want to try the quiz? type ye or no: ')

    if please == 'ye' or please == 'y':
        print('[resume ...]')
        questions()
    else:
        print('goodbye.')
        #ends the program, user didn't want to play :(
        os.kill(os.getpid(),signal.SIGKILL)

def questions():
    score = 0
    print('multiple choice. enter letters from a-e.')
    q1 = input('what is the capital city of belgium?\n a. mexico city\n b. ottawa'
               '\n c. brussels\n d. washington d.c.\n e. bangkok\n > ')
    if q1 == 'c':
        print('\n')
        print('good job, belgium would be proud')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('nope, the answer is brussels')

    q2 = input('what is the capital city of venezuela?\n a. cardiff\n b. buenos aires'
               '\n c. cairo\n d. dublin\n e. caracas\n > ')
    if q2 == 'e':
        print('\n')
        print('good job, that\'s right')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('nope, the answer is caracas')

    q3 = input('how many capital cities does malaysia have?\n > ')
    val1 = int(q3)
    if val1 == 13:
        print('\n')
        print('good job, that\'s correct.')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('nope, the answer is 13')

    q4 = input('how many capital cities does bolivia have?\n > ')
    val2 = int(q4)
    if val2 == 2:
        print('\n')
        print('good job, that\'s correct.')
        score += 1
        print(f'your score: {score}\n')
    else:
        print('nope, the answer is 2')
        
#def again():
    
begin()
