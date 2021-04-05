# This is uncleaned journal.py file
# It includes comments around the save function.

import os # provides os independent path operations. Don't have to worry about slash directions.


'''
This journal module handles the loading and saving of journal entries. It is accessed from the main program file entering 'import journal'

This module has three functions.
The are accessed from program's that import this module.
'''


def load(name):
    # todo: populate from file if it exists.
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name +'.jrl'))
    print('... saving to: \n{}\n'.format(filename))


    # fout = open(filename, 'w') # fout = file output stream
    with open(filename, 'w') close as fout: #this closes fout when done w/ filename
    for entry in journal_data:
        fout.write(entry +'\n')

'''
NOTE: next line not needed with "with open(filename, 'w') close as fout:"
    fout.close() # always want to close file handles when you are done.

'''


# this takes 'text' and adds it to existing journal_data.
def add_entry(text, journal_data):
    journal_data.append(text)


'''
NOTE: This was process in video before using 'import os'
    def save(name, journal_data):
        base_dir = "~/myworkingfolder"
        relative_dir = "data/temp.txt"

        full_file = base_dir + '/' + relative_dir
        filename = './journals/' + name +'.jrl'

#NOTE: fout = file output stream
#NOTE: the 'w' allows you to write to filename.

'''
