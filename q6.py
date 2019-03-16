
import numpy as np


myArray1 = np.array([])

num = int(input('Enter the the number of elements of Array : '))

# Creating array
print('Enter {} elements : \n----------------------------'.format(num))
for i in range(num):
    myArray1 = np.append(myArray1, int(input('Enter a number : ')))


# Display
print(myArray1)


# sum of array
print('Sum of array => ', sum(myArray1))

# sort

print('Sorted Array => ', sorted(myArray1))

# change array shape
# for this we have to make array of size 12
print("modified Array shape => ", myArray1.reshape(3, 4))
