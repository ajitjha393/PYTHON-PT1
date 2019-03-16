class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Student(Person):
    def __init__(self, rollNo):
        self.rollNo = rollNo

    def setCollege(self, college):
        self.college = college

    def getCollege(self):
        return self.college

    def getRollNo(self):
        return self.rollNo


class Employee(Person):
    def __init__(self, empId):
        self.empId = empId


class Intern(Employee, Student):
    def __init__(self, name, gender, empId, rollNo, tenure, college):
        Person.__init__(self, name, gender)
        Employee.__init__(self, empId)
        Student.__init__(self, rollNo)
        Student.setCollege(self, college)
        self.tenure = tenure

    def getDetails(self):
        print('Details are : \n Name \t Gender \t Emp-Id \t Roll no \t Tenure \t College ')
        print(f"{self.getName()} \t {self.getGender()} \t {self.empId} \t {self.getRollNo()} \t {self.tenure} \t  {self.getCollege()}")


name, gender, empId, rollNo, tenure, college = input(
    'Enter name,gender,emp-Id,roll no,tenure,college : ').split(',')
mySmartIntern = Intern(name, gender, empId, rollNo, tenure, college)

mySmartIntern.getDetails()
