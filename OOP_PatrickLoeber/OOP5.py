# Code based on Patrick Loeber tutorial
# https://www.youtube.com/watch?v=-pEs-Bss8Wc
# OOP - Properties => Pythonic way

class SoftwareEngineer:

    def __init__(self):
        self._salary = None
        self._num_bugs_solved = 0

    # getters
    @property
    def salary(self):
        return self._salary
    
    # setter
    @salary.setter
    def salary(self, value):
        self._salary = value


se = SoftwareEngineer()
se.salary = 7000
print(se.salary)

# Recap
# encapsulation
# abstraction
# public, private
# _foo(), _x
# getter / setter
# getter -> #property
# setter -> @x.setter