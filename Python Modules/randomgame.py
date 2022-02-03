'''
Create a guessing Game, user need to guess the correct number
# Requirements
1. generate a number with random module and arguments is pass by user from terminal
2. store the number and ask the prompt from user for correct guess
3. compare the input with random number
    a. if input > number (number is large, please go for low)
    b. if input < number (number is small, please go for higher)
    c. if input == number (congrates you guess it right, whalla!)  

Extra Challenge: change the prompt to ask for the proper Number range Dynamically i.e. Guess a Number 1 ~ 2
'''

from random import randint
from sys import argv


def randomGuessingNumberGame():
    start = int(argv[1])
    stop = int(argv[2])
    random_number = randint(start, stop)
    guesses = 0
    while True:
        try:
            user_guess = int(
                input(f'Enter the choice between {start} and {stop} '))
            guesses += 1
            if 0 < user_guess < (stop+1):
                if random_number < user_guess:
                    print('number is Big, please go for low')
                elif random_number > user_guess:
                    print('number is small, please go for higher')
                else:
                    print(
                        f'congrates you guess it right in {guesses}, whalla!')
                    break
            else:
                print('I said enter a number between 1~10.')
        except Exception as err:
            print(f'Please Give a Valid Input {err}')


if __name__ == '__main__':
    randomGuessingNumberGame()


# ///////////////////////////////////////////////////////////////////////////

# Solution Code -|
# from random import randint
# # you will need to run this on your machine and not this website for the sys.argv to work!
# import sys

# answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#     try:
#         guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
#         if  0 < guess < 11:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('please enter a number')
#         continue
