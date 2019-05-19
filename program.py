# import random #random module or library to get a random number.
#
# print('--------------------------------')
# print('    GUESS THAT NUMBER GAME')
# print('--------------------------------')
# print()
#
# the_number = random.randint(0,100)
#
# guess = -1
#
# while guess != the_number:
#     guess = int(input('Guess a number between 0 and 100: ')) #'int' is a class
#     if guess < the_number:
#         print('The guess is too low.')
#     elif guess > the_number:
#         print('The guess is too high.')
#     else:
#         print('You win!')

import random

print('------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('------------------------------------')

number = random.randint(0,100)

guess = -1

while guess != number:
    guess = int(input('Guess a number between zero and one hundred: '))
    if guess < number:
        print('Too low. Guess again.')
    elif guess > number:
        print('Too high. Guess again.')
    else:
        print('Correct, you win!')
