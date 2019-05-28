import os

'''
Note that os.path.exists returns true
if there's anything with the name
passed as argument, be it file or directory.
'''


if os.path.isfile('~/myfile'):
    print('This file exists.')
else:
    print('File not found')


if os.path.isdir('~/mydir'):
    print('This directory exists.')
else:
    print('This directory does not exits.')
