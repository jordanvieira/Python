# Escrever e explicar um programa de computador para
# achar o produto de menor custo entre n matrizes,
# usando programação dinâmica.
# pip3 install numpy

import sys
import numpy as np
infinito = np.inf


def f(i, j):
    return str(i)+','+str(j)


def MultM(d):  # a entrada d é caracterizada como o exemplo: matrizes 10x20, 20x50, 50x1, 1x100  = (10,20,50,1,100)
    n = len(d)-1  # numero de matrizes a serem multiplicadas
    # m[i,j] guardará o menor numero de operacoes para se multiplicar as matrizes de i a j;
    m, s = {}, {}
    for i in range(1, n+1):
        # salva em m[i,i] o numero de operacoes com uma unica matriz = 0
        m[f(i, i)] = 0
    for l in range(2, n+1):  # inicia com cadeia de duas matrizes: l=2 e vai aumentando
        for i in range(1, n-l+2):
            j = i+l-1
            m[f(i, j)] = infinito  # m[i,j] = infinito
            # k onde irar cortar os parenteses| obtencao de m[i,j] por meio de solucao de recursao:
            for k in range(i, j):
                # aqui entra programacao dinamica, pois varios valores da ->
                q = m[f(i, k)]+m[f(k+1, j)]+d[i-1]*d[k]*d[j]
                # arvore de recursao ja foram calculados e sao trazidos de m
                if q < m[f(i, j)]:
                    # obtencao de m otimo para multiplicacao da cadeia de matrizes de i a j
                    m[f(i, j)] = q
                    # onde ocorreu a divisao otima da cadeia de matrizes de i a j
                    s[f(i, j)] = k
    return m, s


def Parenteses(s, i, j):
    res = ''
    if i == j:
        return "M"+str(j)
    else:
        res += "("
        res += Parenteses(s, i, s[f(i, j)])
        res += Parenteses(s, s[f(i, j)]+1, j)
        res += ")"
        return res


d = [10, 20, 50, 1]
m, s = MultM(d)


print('Melhor Custo：', m[f(1, len(d)-1)])
print('Solução ótima:', Parenteses(s, 1, len(d)-1))
