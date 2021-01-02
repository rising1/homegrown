# *********************************************************************
# *********************Utility function for matrix operations**********
# *********************************************************************

def dotOperation( operation, matrix1, matrix2):
    print("matrix1= ",matrix1, " matrix2= ", matrix2)
    a = len(matrix1)
    b = len(matrix1[0])
    c = len(matrix2)
    d = len(matrix2[0])

    if (a == d and b == c):
        matrix1 = reshape(matrix1)
    result = [[0 for col in range(d)] for row in range(c)]
    for i in range(c):
        for j in range(d):
            if operation == "multiply_elements":
                result[i][j] = matrix1[i][j] * matrix2[i][j]
            if operation == "add_elements":
                result[i][j] = matrix1[i][j] + matrix2[i][j]

    if (a > c and b == c):
        result = [[0 for col in range(b)] for row in range(a)]
        for i in range(a):
            for j in range(b):
                if operation == "multiply_elements":
                    result[i][j] = matrix1[i][j] * matrix2[j][j]
    return result


def addVector( vector):
    sum = 0.0
    for w in range(len(vector)):
        for v in vector[w]:
            sum += v
    return [[sum]]


def multiplyVector( scalar, vector):
    if not isinstance(vector, int):
        for v in vector:
            v[0] = v[0] * scalar
    return vector


def reshape( matrix):
    a = len(matrix)
    if (not isinstance(matrix[0], int)):
        b = len(matrix[0])
        newMatrix = [[0 for col in range(a)] for row in range(b)]
        for i in range(a):
            for j in range(b):
                newMatrix[j][i] = matrix[i][j]
    else:
        newMatrix = [[0] for col in range(a)]
        for i in range(a):
            newMatrix[i][0] = matrix[i]
    return newMatrix

def buildMatrix(matrix1,matrix2):
    a = len(matrix1)
    c = len(matrix2)
    newMatrix = [[0.5 for col in range(c)] for row in range(a)]
    print("buildMatrix= ",newMatrix)
    return newMatrix



def printMatrixShape(self, matrix1):
    print("matrix1 shape= (", len(matrix1), len(matrix1[0]), ")")

# **************************************************************
# *************** End of utility functions *********************
# **************************************************************