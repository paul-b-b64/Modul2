def get_matrix(n, m, value):
    matrix = []
    line_ = []
    for i in range(n):
        matrix.insert(i, line_)
    for j in range(m):
        line_.insert(j, value)
    return matrix
result1 = get_matrix(2,2,10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)







