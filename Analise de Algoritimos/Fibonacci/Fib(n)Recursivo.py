# Algoritmo Recursivo
import time
inicio = time.time()


def fib(n):
    if (n >= 2):
        return(fib(n-1) + fib(n-2))
    else:
        return(n)


fim = time.time()
y = fim - inicio
print(y)
fib(50)
