#Class notes from Corey Shafer's videos on Youtubeself.
#Class variables are shared with the classself.
#Instance variables are unique to an instance.

class employee:

    def __init__(self, first, last, pay): #Instance variables for the employee class.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * 1.05)

emp1 = employee('Gaither', 'McKracken', 70000)
emp2 = employee('Test', 'User', 50000)




#another example to understand the two variable types: Class and instance variables.
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


class MyClass(object):
     i = 123
     def __init__(self):
         self.i = 345

a = MyClass()
print (a.i, 'This is a instance variable example.')
# 345
print (MyClass.i, 'This is a class variable example.')
# 123
