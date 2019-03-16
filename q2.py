
#-----Just do menu driven part by yourself ---------------#
import numpy as np


def isSymmetric(row, col, Matrix1):
    for i in range(0, row):
        for j in range(0, col):
            if(i != j and Matrix1[i, j] != Matrix1[j, i]):
                return False
    return True


row, col = input('Enter the number of row and col of the matrix : ').split(',')
row, col = int(row), int(col)
myList = input(
    "Enter the Elements of matrix 1 of order ({} x {}) ".format(row, col)).split()
Matrix1 = np.matrix(list(map(int, myList))).reshape(row, col)

transposeMatrix = Matrix1.transpose()
print("Transpose of matrix => ", transposeMatrix)


if isSymmetric(row, col, Matrix1):
    print('Entered Matrix is Symmetric. ')
else:
    print('Enterd Matrix is non-symmetric. ')
