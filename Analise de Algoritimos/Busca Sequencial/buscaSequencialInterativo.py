A = list(range(1, 11))


def Decide(A, n, x):
    i = 0
    while i <= n and A[i] != x:
        i = i + 1
    if i > n:
        return False
    else:
        return True


Decide(A, 10-1, 5)
