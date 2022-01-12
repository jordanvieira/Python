#Algoritmo recursivo:
A = list(range(1, 101))


def max_r(A, n):
    if n == 1:
        return A[1]
    else:
        x = max_r(A, n - 1)
        if x < A[n - 1]:
            return A[n]
        else:
            return x


max_r(A, 100)
