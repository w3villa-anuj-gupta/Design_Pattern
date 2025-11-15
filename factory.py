# Factory Pattern : Employee Factory

from observer import EmployeeObserver

class EmployeeFactory:
    def create_employee(self, role, name):
        if role == "Developer":
            return Developer(name)
        elif role == "Manager":
            return Manager(name)
        else:
            raise ValueError("Invalid role specified")

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee, EmployeeObserver):
    def __init__(self, name):
        super().__init__(name)
class Manager(Employee, EmployeeObserver):
    def __init__(self, name):
        super().__init__(name)
