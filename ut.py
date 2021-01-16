# Matrix utilities


def m(op, m1, m2):
    # print("matrix1 = ", m1, " matrix2 = ", m2, " op= ", op)
    row1, col1 = m_type(m1)
    row2, col2 = m_type(m2)
    if row1 == 0:
        m1 = [m1]
        row1, col1 = m_type(m1)
    # print("row1=", row1, " col1=", col1, "row2=", row2, " col2=", col2)

    if op == 'dot':
        result = [[0 for col in range(col2)] for row in range(row1)]
        # print("result=", result)
        for i in range(row1):
            for j in range(col1):
                for y in range(col2):
                    result[i][y] = result[i][y] + m1[i][j] * m2[j][y]
        return result

    if op == 'mult':
        result = [[0 for col in range(col2)] for row in range(row1)]
        # print("result=", result)
        for i in range(row1):
            for j in range(col1):
                for y in range(col2):
                    result[i][y] = m1[i][j] * m2[j][y]
        return result

    if op == 'add':
        if not (row1 == row2 and col1 == col2):
            m1 = reshape(m1)
            row1, col1 = m_type(m1)
        result = [[0 for col in range(col1)] for row in range(row1)]
        for i in range(row1):
            for j in range(col1):
                result[i][j] = m1[i][j] + m2[i][j]
        return result

    if op == "minus":
        if not (row1 == row2 and col1 == col2):
            m1 = reshape(m1)
            row1, col1 = m_type(m1)
        result = [[0 for col in range(col1)] for row in range(row1)]
        for i in range(row1):
            for j in range(col1):
                result[i][j] = m2[i][j] - m1[i][j]
        return result

    if op == "mse":
        if not (row1 == row2 and col1 == col2):
            m1 = reshape(m1)
            row1, col1 = m_type(m1)
        result = [[0]]
        for i in range(row1):
            for j in range(col1):
                result[0][0] = result[0][0] + (m2[i][j] * m1[i][j])
        result[0][0] = result[0][0] / col1
        return result

def times(scalar1, scalar2, m1):
        row1, col1 = m_type(m1)
        result = [[0 for col in range(col1)] for row in range(row1)]
        for i in range(row1):
            for j in range(col1):
                result[i][j] = m1[i][j] * scalar1 * scalar2
        return result

def m_type(matrix):
    if isinstance(matrix[0], int):
        row = 0
        col = len(matrix)
    else:
        row = len(matrix)
        col = len(matrix[0])
    # print("row=", row, " col=", col)
    return [row, col]

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

def buildMatrix(matrix1,matrix2,val):
    a = len(matrix1)
    c = len(matrix2)
    newMatrix = [[val for col in range(c)] for row in range(a)]
    # print("buildMatrix= ",newMatrix)
    return newMatrix

def Relu(matrix):
    a = len(matrix)
    b = len(matrix[0])
    for i in range(a):
        for j in range(b):
            if matrix[i][j] > 0:
                continue
            else:
                matrix[i][j] = 0
    return matrix




if __name__ == "__main__":
    test_matrix1 = [[0, 0, 1]]
    test_matrix2 = [[0.5, 0.5, 0.5],
                    [0.5, 0.5, 0.5],
                    [0.5, 0.5, 0.5],
                    [0.5, 0.5, 0.5]]
    m("mult",test_matrix1,test_matrix2)