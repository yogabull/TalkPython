# notes on the datetime module and classes

#this imports the datetime module which lets you work with dates and times.
# import datetime

# A namespace is a mapping from names to objects.
# https://docs.python.org/3/tutorial/classes.html
# the module object and attribute occupy the same namespace

# example:
# datetime.datetime
# the first "datetime" is the module object
# the ".datetime" is the attribute

# example 2:
# modname.funcname
# modname is the module object (global name defined in the module)
# .funcname is an attribute of modname

# example 3:
# z.real, real is an attribute of z

def scope_test():
    def do_local():
        spam = "local spam"


    def do_nonlocal():
        # nonlocal spam
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