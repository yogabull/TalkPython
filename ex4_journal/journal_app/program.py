# This is journal application

import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------')
    print('       Journal App')
    print('----------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = "EMPTY"
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd: # the truthiness of empty collections (strings) is false.
        cmd = input('List entries [L], Add entry [A], or exit [x]: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd: # another empty 'cmd' test which asks if it is false.
            print("I don't understand {}.".format(cmd))
    print('\nGoodbye\n')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('\nYour Journal Entries:')
    entries = reversed(data) # this reverses order of the data entries.
    # for entry in enumerate(entries): # idx adds an index with each entry.
    for idx, entry in enumerate(entries): # 2 itmes in tuple 'entries' assigned to 2 local varibles.
            print('[{}], {}'.format(idx + 1, entry))# idx+1 starts the counter at 1 instead of zero.
    print(data, type(data))


def add_entries(data):
    text = input('Write an entry: ')
    journal.add_entry(text, data)


main()
