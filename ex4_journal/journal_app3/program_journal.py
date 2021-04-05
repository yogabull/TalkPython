"""Journal App Exercise 05"""
import journal


def main():
    header()
    run_event_loop()
    end()


def header():
    print('-------------------------')
    print('      Journal App')
    print('-------------------------')


def run_event_loop():
    print('Welcome to your journal.')
    cmd = 'EMPTY'
    journal_name = "default"
    journal_data = journal.load(journal_name)

    print("Enter [a] to add an entry.")
    print("Enter [l] to list the entries.")
    print("Enter [x] to exit.")
    while cmd != 'x' and cmd:
        cmd = input('> ')
        cmd = cmd.strip().lower()
        if cmd == 'a':
            add_entry(journal_data)
        elif cmd == 'l':
            list_entries(journal_data)
        elif cmd != 'x' or cmd:
            print(f"I don't understand '{cmd}'.")
            print("Please try again: ")

    print('\nDone. Goodbye.')
    journal.save(journal_name, journal_data)


def add_entry(data):
    text = input('Make entry: ')
    journal.add_entry(text, data)
    # data.append(entry) # Do not like because it is adjusting things directly.


def list_entries(data):
    print('Your journal entries: ')
    print('-----------------------')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(f"{idx+1}: {entry}")
    print('-----------------------')


def end():
    print()
    print('=========================')


if __name__ == "__main__":
    main()
