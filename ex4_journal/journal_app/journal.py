import os # provides os independent path operations. Don't have to worry about slash directions.

'''
This journal module handles the loading and saving of journal entries.
'''


def load(name):
    # todo: populate from file if it exists.
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin: #fin = file input
            for entry in fin.readlines():
                # print('would load: ' + entry.rstrip())
                data.append(entry.rstrip())
    return data



     # proper os independent style uses '.' in filename = ...
def save(name, journal_data):
    filename = get_full_pathname(name)
    print('... saving to: \n{}\n'.format(filename))

    with open(filename, 'w') as fout: #this closes as fout when done w/ filename
        for entry in journal_data: # loop iterates through each journal entry.
            fout.write(entry +'\n')


# this method created because it is used twice to save and load.
def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals/', name +'.jrl'))
    return filename


# this takes 'text' and adds it to existing journal_data.
def add_entry(text, journal_data):
    journal_data.append(text)


'''
made a method from this second line that was under the save function:
    filename = os.path.abspath(os.path.join('.', 'journals/', name +'.jrl'))
'''
