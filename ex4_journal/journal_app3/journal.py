"""Journal module with the logic to add and save entries."""
import os


def load(name):
    """
    This method creates and loads a new journal.

    param name: This is base name of journal to load.\n 
    return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename, 'r') as fin:  # file input stream
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print(f"... saving to {filename}")

    """This is an alternate version that closes without needing to be done explicitly."""
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
