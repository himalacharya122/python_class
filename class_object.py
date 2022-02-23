class Employee:

    def __init__(self, name, salary, taxP):
        self.name = name
        self.salary = salary
        self.tax = taxP

    def NetSalary(self):
        NetSalary = self.salary - (self.salary*self.tax)/100
        return NetSalary


Em1 = Employee("Vekh Raj", 18000, 13)
Em2 = Employee("sujan", 20000, 14)

print(Em1.NetSalary())
print(Em2.NetSalary())