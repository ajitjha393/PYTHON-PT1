import array as arr
dataType = input('Enter the data type of array : ')
# i -> int
# f -> float
# d -> double
# l -> long

if dataType == 'int':
    d = 'i'
    fun = int
elif dataType == 'float':
    d = 'f'
    fun = float

myArray = arr.array(d, [])

num = int(input('Enter the the number of elements of Array : '))

# Creating array
print('Enter {} elements : \n----------------------------'.format(num))
for i in range(num):
    myArray.append(fun(input('Enter a number : ')))

# Display
print(myArray)

# Insert an element at end

myArray.append(fun(input('Enter the element to be added at end : ')))
print('After appending => ', myArray)

# Delete an element from beg

myArray.pop(0)
print('After deleting => ', myArray)
# sort

print('Sorted Array => ', sorted(myArray))
