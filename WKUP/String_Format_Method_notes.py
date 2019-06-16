'''
The String format() Method or
string.format()

ie:
'''
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# or

print('We are the {0} who say "{1}!"'.format('knights', 'Ni'))

# or

print('The story of {0}, {1} and {other}.'.format('Bubba', 'Elle', other = 'Nermal'))
print('This statement uses positional and key word arguements.')

table = {'Elle':1234, 'Corbin':5678, 'John':9012}
print(type(table))
print('Corbin : {0[Corbin]:d}, Elle : {0[Elle]:d}'.format(table))

print('\nYou can remove the table positional index if you put ** before the format() argument. ie .format(**table)\n')

print('Corbin : {Corbin:d}\nElle : {Elle:d}\n'.format(**table))

for i in range(1, 11):
    print('{0:2d} -- {1:3d} -- {2:4d}'.format(i, i*i, i*i*i))
    # I think the ':2d' within {0:2d} designates a mininum number of spaces to print.

'''
https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
'''
