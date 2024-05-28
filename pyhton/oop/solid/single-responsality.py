"""
Single Responsability:
    - Cada clase debe tener una sola responsabilidad.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_payroll(self):
        return self.salary

class PayrollSystem:
    def calculate_payroll(self, employees):
        return sum(employee.calculate_payroll() for employee in employees)
