# #Tarefa 11
import time
inicio = time.time()


def F(n):
    if n == 0:
        return 10
    x = F(n-1) + n + 1
    return x


fim = time.time()
y = fim - inicio
print(f"Tempo de execução: {y}")
F(950)

# Fórmula fechada e solução da recorrência
# F(0) = 1
# n = 10
# print((n**2 + 3*n + 20)/2)

# Fórmula fechada e solução da recorrência
# F(0) = 10
# n = 1000
# print((n**2 + 3*n + 20)/2)
