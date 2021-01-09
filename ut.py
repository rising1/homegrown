# Matrix utilities


def m(op, m1, m2):
    print("matrix1 = ", m1, " matrix2 = ", m2, " op= ", op)
    row1, col1 = m_type(m1)
    row2, col2 = m_type(m2)
    print("row1=", row1, " col1=", col1, "row2=", row2, " col2=", col2)
    result = [[0 for col in range(col1)] for row in range(row2)]
    print("result=", result)

def m_type(matrix):
    if isinstance(matrix[0], int):
        row = 0
        col = len(matrix)
    else:
        row = len(matrix)
        col = len(matrix[0])
    print("row=", row, " col=", col)
    return [row, col]


if __name__ == "__main__":
    test_matrix1 = [[0, 0, 1]]
    test_matrix2 = [[0.5, 0.5, 0.5],
                    [0.5, 0.5, 0.5],
                    [0.5, 0.5, 0.5],
                    [0.5, 0.5, 0.5]]
    m("mult",test_matrix1,test_matrix2)