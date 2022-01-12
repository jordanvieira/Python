a = list(range(1, 101))


def soma_dir_esq(k, n, a):
    if k > n-1:
        s = 0
    else:
        s = a[k] + soma_dir_esq(k+1, n, a)
        print(s,  end=" ")
    return s


soma_dir_esq(0, 100, a)
