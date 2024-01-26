# sum_of_squares_cython.pyx

def sum_of_squares_cython(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result
