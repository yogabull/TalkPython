


'''
//////////////////////


# Class exercise from: https://www.learnpython.org/en/Classes_and_Objects

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = 'Fer'
car1.kind = 'Convertible'
car1.color = 'Red'
car1.value = 600000

car2 = Vehicle()
car2.name = 'Jump'
car2.kind = 'Van'
car2.color = 'Blue'
car2.value = 100000

c3 = ('Old Brown', 'Hatchback', 'brown', 2000)
car3 = Vehicle()
car3.name = c3[0]
car3.kind = c3[1]
car3.color = c3[2]
car3.value = c3[3]

c4 = ('Black Bat', 'hooptie', 'black', 300)
car4 = Vehicle()
car4.name = c4[0]
car4.kind = c4[1]
car4.color = c4[2]
car4.value = c4[3]

# test code
print(car1.description())
print(car2.description())
print(car3.description())
print(car4.description())

print()
print("{}'s variables were populated with individual strings.".format(car2.name))
print("{}'s variables were populated from a tuple.".format(c3[0]))
print("{}'s variables were populated from a tuple and is worth only {}".format(car4.name,str(car4.value)))

print('\nIt might be faster to code class variables from tuples rather than hard-coding individual string variables.\n')


//////////////////

# Classes exercise from: https://www.learnpython.org/en/Classes_and_Objects
# def list_benefits():
#     return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
#
#
# def build_sentence(benefit):
#     return benefit + " is a benefit of functions!"
#
#
# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
#
# name_the_benefits_of_functions()
