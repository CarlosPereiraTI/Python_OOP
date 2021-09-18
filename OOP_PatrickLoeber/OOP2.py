# Code based on Patrick Loeber tutorial
# https://www.youtube.com/watch?v=-pEs-Bss8Wc
# OOP - Functions in classes


# position, name, age, level, salary
# se1 = ["Software Engineer", "Charlie", 34, "Junior", 5000]
# se2 = ["Software Engineer", "Max", 41, "Senior", 7000]
# d1 = ["Designer", "John", 30, "Junior", 4000]
# this is not a good method to represent an object

# Not a good way to handle it
# def code(se):
#     print(f"{se[1]} is writing code...")

# code(d1)
# this will show "John is writing code" but he is not a developer


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
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{ self.name } is writing code...")

    def code_in_language(self, language):
        print(f"{ self.name } is writing code in { language }.")

    # def information(self):
    #     information = f"name: { self.name } | age: { self.age } | level: { self.level }"
    #     return information

    # string representation
    # dunder method
    def __str__(self):
        information = f"name: { self.name } | age: { self.age } | level: { self.level }"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance of the class
se1 = SoftwareEngineer("Charlie", 34, "Junior", 5000)
# print(se1.name, se1.age, se1.level, se1.salary)
se2 = SoftwareEngineer("Max", 41, "Senior", 7000)
se3 = SoftwareEngineer("Max", 41, "Senior", 7000)
# print(se2.name, se1.age, se1.level, se1.salary)

# print(SoftwareEngineer.alias)
# print(se1.alias)
# print(se2.alias)

se1.code()
se1.code_in_language("Python")
se2.code()
se2.code_in_language("Java")

# info = se1.information()
# print(info)
print(se1)
print(se2 == se3)

print(se1.entry_salary(24)) # This will crash without the decorator
print(SoftwareEngineer.entry_salary(42))


# Recap
# - Instance method (self)
# - can take arguments and return values
# - special "dunder" method (__str__ and __eq__)
# - @staticmethod
