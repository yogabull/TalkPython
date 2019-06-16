# Notes from the python docs showing scopes and namespace
# taken from: https://docs.python.org/3/tutorial/classes.html

# A namespace is a mapping from names to objects.
# https://docs.python.org/3/tutorial/classes.html
# the module object and attribute occupy the same namespace

def scope_test():
    def do_local():
        spam = "local spam"


    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"


    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print()
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
