'''First custom module to print info on objects'''


def wt(obj):
    """Pass in an object, prints the object and what it is."""
    print('========== THIS THING IS: ==========')
    print()
    print(obj)
    print()
    print(type(obj))
    print()
    print("====================================")

    if type(obj) == tuple:
        print('------ This is a tuple. ------')
        print('     Unpacking this sucka: ')
        print()

        for idx, i in enumerate(obj):
            print(f"------ Item {idx} ------")
            print(i)
            print(type(i))
            print()

    else:
        print('This does not contain a tuple.')
