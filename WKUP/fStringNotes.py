#fString exercise from link at bottom

table = {'John' : 1234, 'Elle' : 4321, 'Corbin' : 5678}
for name, number in table.items():
    print(f'{name:10}  -->  {number:10d}')

# John        -->        1234
# Elle        -->        4321
# Corbin      -->        5678

'''
NOTE: the '10' in {name:10} means make the name variable occupy at least 10 spaces.
This is useful for making columns align.
'''

'''
f-Strings:
    Another method to output varibles within in a string.
    Formatted String Literals
    This reads easily.

    year = 2019
    month = 'June'
    f'It ends {month} {year}.'
    >>> It ends June 2019.

    https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
'''
