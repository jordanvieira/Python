A = list(range(1, 101))


def Decide(A, n, x):
    if n == 0:
        return False

    if A[n-1] == x:
        return True
    else:
        return Decide(A, n-1, x)


Decide(A, 100, 102)
