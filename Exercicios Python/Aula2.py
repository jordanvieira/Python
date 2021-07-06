# -*- coding: utf-8 -*-
numero = input ("digite sua idade:")
print ("sua idade é :", numero)


####### Função#####

def soma(x , y):
    print (x + y)
soma(2, 3)

######## arquivos #####

w = open("arquivo.txt", "a")
w.write("esse é o meu arquivo\n")

w.close()

##### lista #####
minha_lista = ["eu"," sei", "nada", 1, 2, 3]

print (minha_lista[2])

for item in minha_lista:
    print (item)
  
minha_lista.append(6) 
print(minha_lista)
#####lista 2####
lista = [123,454, 67, 7 ,6 ,4 ,5 ,1, 0]
lista.sort()
print(lista)

lista.reverse()
print(lista)

##### dicionario####


