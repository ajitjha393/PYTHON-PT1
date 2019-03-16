class Employee:
    empCount = 0

    def __init__(self, id, dept, salary):
        self.id = id
        self.dept = dept
        self.salary = salary

    def setName(self, name):
        self.name = name

    def display(self):
        print(f"{self.id} \t {self.name} \t {self.dept} \t {self.salary} ")

    @classmethod
    def setEmpCount(cls):
        cls.empCount += 1

    @classmethod
    def getEmpCount(cls):
        return cls.empCount


myEmployeeList = []

num = int(input('\nEnter the number of Employees : '))

for i in range(0, num):
    print('Enter the details of  Employee {} :\n----------------------------------------------'.format(i+1))
    myEmployeeList.append(Employee(int(input('Enter the Id of Employee : ')), input(
        'Enter the department : '), int(input('Enter the Salary : '))))
    myEmployeeList[i].setName(input('Enter the name of Employee : '))
    Employee.setEmpCount()

print('Total Number of Employees => {}'.format(Employee.getEmpCount()))

print("EmpId \t  Name \t  Department \t  Salary \n--------------------------------------------")

for i in range(0, num):
    myEmployeeList[i].display()
