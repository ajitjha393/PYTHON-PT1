import numpy as np


myArray1 = np.array([])

num = int(input('Enter the the number of elements of Array : '))

# Creating array
print('Enter {} elements : \n----------------------------'.format(num))
for i in range(num):
    myArray1 = np.append(myArray1, int(input('Enter a number : ')))


# Display
print(myArray1)

# Compare


myArray2 = np.array([])

num = int(input('Enter the the number of elements of Array 2 : '))

print('Enter {} elements : \n----------------------------'.format(num))
for i in range(num):
    myArray2 = np.append(myArray2, int(input('Enter a number : ')))

myComparison = myArray1 <= myArray2

print(myComparison)


# Display 2nd and 4th element of second row

# For this we create 2d array of size 3 * 4
myArray1 = myArray1.reshape(3, 4)
print('Second Element of Row 2 of Array 1=> ', myArray1[1:2, 1:2])
print('Fourth Element of Row 2 of Array 1=> ', myArray1[1:2, 3:4:])
