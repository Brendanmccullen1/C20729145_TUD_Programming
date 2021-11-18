# Tutorial OOP
# Week 9
# Scope of Variables, Composition and Aggregations
# author: B. Schoen-Phelan
# date: Nov 2021
# some of the examples in this tutorial are taken from other
# sources. For references please see the accompanying
# lecture slides for this week.

# scope of a variable, first without classes

greeting = "Hello World"


def change_greeting(new_greeting):
    greeting = new_greeting


def greeting_world():
    world = "World"
    print(greeting, world) # you can access the variable for reading but not for writing
#
#
change_greeting("Hi")
greeting_world()

# with global scope
greeting = "Hello World"


def change_greeting(new_greeting):
    global greeting
    greeting = new_greeting


def greeting_world():
    world = "World"
    print(greeting, world)


change_greeting("Hi")
greeting_world()


# enclosing scope

def outer():
    first_num = 1

    def inner():
        first_num = 0 # not the same as above
        second_num = 1  # local to the inner function
        print("inner - second_num is: ", second_num)
        print("inner - first num is: ", first_num)

    inner()
    print("outer - first_num is: ", first_num)

outer()



# now with nonlocal flag
def outer():
    first_num = 1

    def inner():
        nonlocal first_num
        first_num = 0
        second_num = 1
        print("inner - second_num is: ", second_num)
        print("inner - first num is: ", first_num)

    inner()
    print("outer - first_num is: ", first_num)


outer()



# scope of variables in ifs, try...except and loops

today = "Monday"

if today == "Monday":
    tomorrow = "Tuesday"

# outside of the block defining tomorrow we have access
print(tomorrow)

for runner_var in range(0,2):
    print(runner_var)
    var1 = runner_var

print("outside the loop: ", var1) # we still have access to it
# try these examples in C and see what happens!


# instance vs class variables
class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, f_name, l_name):
        if title not in self.TITLES:
            raise ValueError("Not a valid title: ", title)

        self.title = title
        self.first_name = f_name
        self.last_name = l_name


p = Person("Ms", "Bianca", "Phelan")
print(p.first_name)
print(p.TITLES)
print(Person.TITLES)
Person.first_name




# Overriding a method

class ClassA:
    def play_game(self):
        print("Playing in ClassA")

class ClassB(ClassA):
    def play_game(self):
        # super().play_game()
        print("Playing in ClassB")

b = ClassB()
b.play_game()





# with calling explicit Classes
class ClassA:
    def play_game(self):
        print("Playing in ClassA")


class ClassB(ClassA):
    def play_game(self):
        print("In ClassB")
        super().play_game()


class ClassC(ClassB):
    def play_game(self):
        print("In ClassC")
        super().play_game()
        ClassA().play_game()


c = ClassC()
c.play_game()

print(ClassC.mro())

#
#
# Composition and Aggregation with
# Employee and Salary example
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus

#
# composition:

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary_object = Salary(pay, bonus) # here is the salary object!!!

    def total_salary(self):
        return self.salary_object.annual_salary()


anna = Employee("Anna", 25, 2500, 10000)
print(anna.total_salary())


# aggregation:

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary_object = salary

    def total_salary(self):
        return self.salary_object.annual_salary()


sal = Salary(2500, 10000)
anna = Employee("Anna", 25, sal) # here is the salary object!
print(anna.total_salary())
#
#
#
#
#
