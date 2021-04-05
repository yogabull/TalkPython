# notes on the datetime module and classes

import datetime

'''
The above line imports the datetime module.
This lets you work with dates and times.
It creates objects with the class 'datetime'
'''

print('\nUsing datetime.datetime creates a class by the same name.')
day1 = datetime.datetime(2055, 5, 5)
day2 = datetime.datetime(2011, 1, 1)
print(day1, type(day1))

print('\nUsing datetime.date creates a class by the same name.')
print(datetime.date(2019, 1, 1))
print(type(datetime.date(2019, 1, 1)))

print('\nThis next line of code creates a date from two different day variables.')
some_date = datetime.date(day1.year, day2.month, day2.day)
print(some_date)

another_date = datetime.date(2021, day1.month, day2.day)
print('Here is another date created with an integer and the .month and .day methods.')

'''
example:
datetime.datetime
the first "datetime" is the module object
the ".datetime" is the attribute

example 2:
modname.funcname
modname is the module object (global name defined in the module)
.funcname is an attribute of modname

example 3:
z.real, real is an attribute of z

A namespace is a mapping from names to objects.
https://docs.python.org/3/tutorial/classes.html
the module object and attribute occupy the same namespace


'''
