# Journal append

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
    journal_data = []

    while cmd != 'x':
        cmd = input('[A] Add entry, [L] List entry, [X] Exit: ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print(f"Sorry, I don't understand {cmd}. ")
    print('Thanks, Goodbye.')



def list_entries(data):
    print(data)


def add_entry(data):
    text = input('Type your entry. <Enter> to exit. \n')
    data.append(text)


main()
