def matrix_addition(matrix1, matrix2):
    result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def matrix_multiplication(matrix1, matrix2):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix1 = [[1, 2],[3, 4]]
matrix2 = [[5, 6],[7, 8]]
print(matrix_addition(matrix1, matrix2))
print(matrix_multiplication(matrix1, matrix2))
print(matrix_transpose(matrix1))