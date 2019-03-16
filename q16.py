def createSet():
    return set(map(int, input('Enter the elements of set  : ').split(',')))


def displaySet(mySet, name):
    print(f"Set {name}=> {mySet}")


def intersection(setA, setB):
    return setA.intersection(setB)


def Union(setA, setB):
    return setA.union(setB)


def setDifference(setA, setB):
    return setA.difference(setB)


def symDifference(setA, setB):
    return setA.symmetric_difference(setB)


myChoice = True
setA = {}
setB = {}
while(myChoice != '7'):
    print('''
        1. Read two sets A and B
        2. Display Set
        3. Perform A n B
        4. Perform A U B
        5. Perform A - B
        6. Perform A exor B 
        7. Exit
        
        ''')
    myChoice = input("Enter a choice : ")

    if myChoice == '1':
        setA = createSet()
        setB = createSet()
    elif myChoice == '2':
        displaySet(setA, 'A')
        displaySet(setB, 'B')
    elif myChoice == '3':
        print(f"Intersection A n B => {intersection(setA,setB)}")
    elif myChoice == '4':
        print(f"Union A n B => {Union(setA,setB)}")
    elif myChoice == '5':
        print(f"Difference A n B => {setDifference(setA,setB)}")
    elif myChoice == '6':
        print(
            f"Symmetric Difference A n B => {symDifference(setA,setB)}")
