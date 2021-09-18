# Code based on Patrick Loeber tutorial
# https://www.youtube.com/watch?v=-pEs-Bss8Wc
# OOP - Encapsulation

class SoftwareEngineer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = 5000         # protected
        self._num_bugs_solved = 0   # protected
        # self.__salary = 5000        # private
        # self.__num_bugs_solved = 0  # private

    def code(self):
        self._num_bugs_solved += 1

    # getters
    def get_salary(self):
        return self._salary

    # setters
    # def set_salary(self, base_value):
    #     # check value, enfort constraints
    #     if base_value < 1000:
    #         self._salary = 1000
    #     if base_value < 20000:
    #         self._salary = 20000
    #     self._salary = base_value

    def set_salary(self, base_value):
        # check value, enfort constraints
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Charlie", 34)
print(se.name, se.age)

for i in range(70):
    se.code()

se.set_salary(7000)
print(se.get_salary())

