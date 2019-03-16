
#-----Just do menu driven part by yourself for rest Questions ---------------#
import numpy as np

myList = input("Enter the Elements of matrix 1 of order (3 x 3) ").split()
Matrix1 = np.matrix(list(map(int, myList))).reshape(3, 3)
myList = input("Enter the Elements of matrix 2 of order (3 x 3) ").split()
Matrix2 = np.matrix(list(map(int, myList))).reshape(3, 3)

while True:
    print('''
    --------------------------------
    1. Matrix Addition 
    2. Matrix Subtraction
    3. Matrix Multiplication
    4. Exit
    ''')
    choice = input('Enter a choice : ')

    if(choice == '1'):
        # Matrix Addition
        matrixAddition = Matrix1 + Matrix2
        print("Matrix 1 + Matrix 2 = {}".format(matrixAddition))

    elif choice == '2':
        # Matrix Subtraction
        matrixSubtraction = Matrix1 - Matrix2
        print("Matrix 1 - Matrix 2 = {}".format(matrixSubtraction))

    elif choice == '3':

        # Matrix Multiplication
        matrixMultiplication = Matrix1 * Matrix2
        print("Matrix 1 * Matrix 2 = {}".format(matrixMultiplication))

    else:
        break
