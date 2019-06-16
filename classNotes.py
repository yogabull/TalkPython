#create an employee class

class employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

# think of the 'self' arguement as the class instance name ie. emp1
emp1 = employee('Gaither', 'McKracken', 30000)
emp2 = employee('test', 'user', 40000)

print(emp1)
print(emp2)
#

print(emp1.email)
print(emp2.email)


'''
NOTES: Classes

Class is blueprint for creating an instance of the classself.
employee class has instances of employees.

why use classes?
They allow us to logically group our data and functions in a way that is easy to reuse and build upon.

data and functions are:
attributes and methods

Methods are functions associated with a class

Instance variables contain info that is unique to the instance.
'''
