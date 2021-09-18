# Code based on Patrick Loeber tutorial
# https://www.youtube.com/watch?v=-pEs-Bss8Wc
# OOP - Inheritance


"""Inheritance is the capability of one class to derive or inherit 
the properties from another class. The benefits of inheritance are: 
... It is transitive in nature, which means that if class B inherits 
from another class A, then all the subclasses of B would automatically 
inherit from class A."""


# inherits, extend, override
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging...")

    def work(self):
        print(f"{self.name} is coding...")

class Designer(Employee):
    
    def draw(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} is designing...")


se = SoftwareEngineer("Charlie",34, 5000, "Senior")
# print(se.name, se.age)
se.work()
# se.debug()
# print(se.level)

de = Designer("Martina", 2, 5000)
# print(de.name, de.age)
de.work()
# de.draw()


# Polymorphism
"""Polymorphism lets us define methods in the child class that have the same 
name as the methods in the parent class"""

employees = [SoftwareEngineer("Charlie", 34, 7000, "Junior"),
             SoftwareEngineer("Max", 41, 17000, "Senior"),
             Designer("Jhon", 27, 5000)]


def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

# Recap
# Inheritance: cild_class(baseclass)
# inherit, extend, override
# super().__init__()
# polymorphism
