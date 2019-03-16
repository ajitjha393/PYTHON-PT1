import array as arr


def getInput():
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
    return fun, myArray


fun, myArray1 = getInput()

# Display
print(myArray1)


# Delete an element from end

myArray1.pop(len(myArray1) - 1)
print('After deleting => ', myArray1)

# Search
print("Element found at index : ", myArray1.index(
    fun(input('Enter the element to be searched : '))))

# Merge Two arrays
print('------------------------------')
fun, myArray2 = getInput()

mergedArray = myArray1 + myArray2
print('Merged Array', mergedArray)

# Reverse

print('Reverse => ', mergedArray[::-1])
