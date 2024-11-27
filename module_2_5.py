#Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list = []
        for j in range(m):
            list.append(value)
        matrix.append(list)
    return (matrix)
result1 = get_matrix(4, 3, 12)
result2 = get_matrix(2, 3, 8)
result3 = get_matrix(5, 4, 2)
print(result1)
print(result2)
print(result3)