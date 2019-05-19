import random #random module or library to get a random number.

print('--------------------------------')
print('    GUESS THAT NUMBER GAME')
print('--------------------------------')
print()

the_number = random.randint(0,100)

guess = -1
name = input('What is your name? ')

while guess != the_number:
    guess = int(input('Guess a number between 0 and 100: ')) #'int' is a class
    if guess < the_number:
        print('Sorry {1}, your guess of {0} is too low.'.format(guess,name))
    elif guess > the_number:
        print('Sorry {}, your guess of {} is too high.'.format(name,guess))
    else:
        print('You win!')

print('All Done {}.'.format(name))

#Using string format converts values into strings. The guess variable is an integer.
