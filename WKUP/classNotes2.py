#create an employee class with attributes and methods (functions related to a class).

class employee:

    def __init__(self, first, last, pay): #this assigns instance variables to the employee class.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def name_info(self): #this is a method called on an instance of the class employee.
        print ('Your first name is {}.'.format(self.first))
        print (f'Your last name is {self.last}.')

    def full_name(self):
        return ('{} {}'.format(self.first, self.last))


emp1 = employee('Gaither', 'McKracken', 30000)
emp2 = employee('Test', 'User', 50000)
emp1.name_info() #This calls the method name_info for emp1.
emp2.name_info() #This calls the method name_info for emp2.


print(emp1.first) #NOTE: the emp1 instance is passed as the self arguement.
print(emp1.email) # printing attribute email for emp1
print(emp1.full_name())
employee.full_name(emp1) #NOTE: This run from the class versus using the class' method.
print('\n\n')

print('These next two lines do the same thing.')
employee.full_name(emp1)
emp1.full_name()
print('NOTE: emp1.full_name()\n is an instance with a method being called on emp1')
print('There is no need to pass "self" in the () because it is done automatically.\n')

print('NOTE: employee.full_name(emp1)\n is a class calling the method full_name that does not know what to pass through it unless you pass emp1 within the ().\n')




'''
    # think of the 'self' arguement as the class instance name ie. emp1
    emp2 = employee('test', 'User', 40000)

    emp2.name_info()
    print()

    print(emp2.full_name())
    print(emp2.full_name)

    print()
    print('=== NOTE: what prints if you do not use "()" after the method.')
    print('=== Not using () returns THE method, not the return value of the method.\n')
'''


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
