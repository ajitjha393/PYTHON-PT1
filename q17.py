class Employee:
    def __init__(self, Name, Salary):
        self.name = Name
        self.salary = Salary

    def __gt__(self, other):
        if self.salary > other.salary:
            return '{} has more salary than {}'.format(self.name, other.name)
        return '{} has more salary than {}'.format(other.name, self.name)


name, salary = input('Enter the name and salary of Employee 1 : ').split(',')
salary = int(salary)
Emp1 = Employee(name, salary)

name, salary = input('Enter the name and salary of Employee 2 : ').split(',')
salary = int(salary)
Emp2 = Employee(name, salary)

print(Emp1 > Emp2)
