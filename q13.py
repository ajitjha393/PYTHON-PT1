#--------Prime Number--------#
def isPrime(myNum):
    for i in range(2, myNum//2 + 1):
        if myNum % i == 0:
            return False
    return True


myNum = int(input('Enter a number : '))
if isPrime(myNum):
    print(myNum, ' is a prime number ')
else:
    print(myNum, ' is not a prime number ')


#-------Perfect Number---------#


def isPerfectNumber(num, findDivisor):
    return sum(findDivisor(num)) == num


def findDivisor(num):
    myDivisorList = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            myDivisorList.append(i)
    return myDivisorList


num = int(input("Enter a number : "))
if isPerfectNumber(num, findDivisor):
    print(f"{num} is a perfect number :)")
else:
    print(f"{num} is not a perfect number :( ")
