# Algoritmo interativo
import time
inicio = time.time()


def fib(n):
    i = 1
    atual = 0
    ultimo = 0
    penultimo = 1
    while (i <= n):
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
        i = i + 1
    return(atual)


fim = time.time()
y = fim - inicio
print(y)
fib(20)
