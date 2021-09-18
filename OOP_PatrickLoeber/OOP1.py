# Code based on Patrick Loeber tutorial
# https://www.youtube.com/watch?v=-pEs-Bss8Wc
# OOP - overview

# position, name, age, level, salary
# se1 = ["Software Engineer", "Charlie", 34, "Junior", 5000]
# se2 = ["Software Engineer", "Max", 41, "Senior", 7000]
# this is not a good method to represent an object

# class
class SoftwareEngineer:

    # class attribute
    # Can be used in the whole class
    # If we do something like print(SoftwareEngineer.alias) or print(se1.alias)
    # both options are valid and should print "Keyboard Magician"
    alias = "Keyboard Magician"
    
    # __init__ is an special method used to initailize the object
    def __init__(self, name, age, level, salary):
        # instance attributes | cannot be used in the whole class
        # We cannot do something like print(SoftwareEngineer.name) => Error
        self.name   = name
        self.age    = age
        self.level  = level
        self.salary = salary


# instance of the class
se1 = SoftwareEngineer("Charlie", 34, "Junior", 5000)
print(se1.name, se1.age, se1.level, se1.salary)
se2 = SoftwareEngineer("Max", 41, "Senior", 7000)
print(se2.name, se1.age, se1.level, se1.salary)

print(SoftwareEngineer.alias)
print(se1.alias)
print(se2.alias)

# Recap
# - How to create a class (blueprint)
# - How to create an instance (object)
# - class vs instance
# - instance attributes defined in __init__(self)
# - class attribute