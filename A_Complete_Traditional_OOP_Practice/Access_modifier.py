
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
        print(f"Employee {self.name} created.")
    
emp = Employee("Sara", 30, 50000)
print(emp.name)        # OK
print(emp._age)     # possible but convention se avoid
print(emp.__salary)       # Error: attribute error
# But name mangling: emp._Employee__ssn works