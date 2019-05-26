# This is journal application

def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------------')
    print('       Journal App')
    print('----------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None

    while cmd != 'x':
        cmd = input('List entries [L], Add entry [A], or exit [x]: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entries()
        elif cmd != 'x':
            print("I don't understand {}.".format(cmd))
    print('\nGoodbye\n')


def list_entries():
    print('\nListing ...')


def add_entries():
    print('\nAdding ...')



main()
