# This file is for working through code snippets.
'''
while True:
    print('enter your name:')
    name = input()
    if name == 'your name':
        break
print('thank you')
'''


"""
name = ''
while name != 'your name':
    name = input('Enter your name: ')
    if name == 'your name':
        print('thank you')
"""
import random

print('-----------------')
print('  Number Game')
print('-----------------')

number = random.randint(0, 100)
guess = ''
while guess != number:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess > number:
        print('Too high')
        print(number)
    if guess < number:
        print('Too low')
        print(number)
    if guess == number:
        print('Correct')
        print(number)

print('---------------------')
print('    f-strings')
print('---------------------')

name = input('Please enter your name: ')
print(f'Hi {name}, it is nice to meet you.')
