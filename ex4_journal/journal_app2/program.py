# make journal app with little help

def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------------')
    print('       Journal App')
    print('---------------------------')
    print()

def run_event_loop():
    print('What do you want to do with your journal? ')
    cmd = None
    journal_data = [] # list()


    while cmd != 'x':
        cmd = input('[L] list entries, [A] add entry, or [X] Exit: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry, I don't understand {}.".format(cmd))

    print('Done. Goodbye.')


def list_entries(data):
    print(data)


def add_entry(data):
    print('Adding ...')



main()
