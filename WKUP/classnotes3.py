#Class notes from Corey Shafer's videos on Youtubeself.
#Class variables are shared with the classself.
#Instance variables are unique to an instance.
# Class variables need tobe applied through the class itself or an instance ofthe class.

class employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): #Instance variables for the employee class.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        employee.num_of_emps += 1

    def full_name(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        # self.pay = int(self.pay * employee.raise_amount)#option 1 apply class variable.
        self.pay = int(self.pay * self.raise_amount)#option 2 apply instance variable.
        #the 2nd version lets you apply a different raise_amount for a single instance.
        #using self lets sub class override that instance raise_amount.


print(employee.num_of_emps, 'number of employees')

emp1 = employee('Gaither', 'McKracken', 70000)
emp2 = employee('Test', 'User', 50000)

print(emp1.pay)
emp1.apply_raise() #this added the attribute to the class.
print(emp1.pay)
print()

emp1.raise_amount = 1.06
print(emp1.__dict__)

print(employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(employee.num_of_emps, 'number of employees')
print('The number of employees changes after the 2 employee classes were instantiated.')

'''
    print('NOTE:\nemp1.__dict__\nproduces this dictionary for emp1:')
    print(emp1.__dict__)
    print()
    print('NOTE:\nemployee.__dict__\nproduces this information for the employee dictionary:')
    print(employee.__dict__)
    print()
'''

'''
    #another example to understand the two variable types: Class and instance variables.
    class MyClass(object):
         i = 123
         def __init__(self):
             self.i = 345

    a = MyClass()
    print (a.i, 'This is a instance variable example.')
    # 345
    print (MyClass.i, 'This is a class variable example.')
    # 123
'''
