# if f'' gives error for u ,then use " {} ".format


def addDetail():
    myStudentList = []
    n = int(input('Enter the number of students : '))
    for i in range(0, n):
        print(f'''
            Enter the detail of Student {i+1} : 
     ----------------------------------------------------
        ''')
        myStudentList.append(
            tuple(input('Enter Name, Roll-no, Marks obtained in 3 Subjects : ').split(',')))
    return myStudentList


def showDetail(myStudentList):
    print(f'''
    Name        Roll-No        S-1        S-2       S-3
    ----------------------------------------------------------
    
    ''')
    for student in myStudentList:
        # print('       ', end='')
        for records in student:
            print(f'''{records}        ''', end='')
        print()


def displayByName(myStudentList, keyName):
    for student in myStudentList:
        if student[0] == keyName:
            return student
    return 'Student record not present'


myChoice = True
myList = []
while(myChoice != '4'):
    print('''
        1.Add Student Record
        2. Display Student Record
        3. Search Student Record by Name
        4. Exit
        
        ''')
    myChoice = input("Enter a choice : ")

    if myChoice == '1':
        myList = addDetail()
    elif myChoice == '2':
        showDetail(myList)
    elif myChoice == '3':
        print(displayByName(myList, input('Enter the name of student : ')))
