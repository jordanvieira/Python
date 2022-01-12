# Algoritmo iterativo:
A = list(range(1, 11))


def max(A, n):
    x = A[0]
    for i in range(2, 10):
        if A[i] > x:
            x = A[i]
    return x


max(A, 5)
