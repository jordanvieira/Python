# -*- coding: utf-8 -*-
'''
Calculadora
Autor: Jordan Vieira
'''


print ("----- Calculadora v2.0-----")

sair = False
while sair == False:

	num1 = input("Digite o primeio número:")
	num1 = int(num1)
	ope = input("Digite o operador (+,-,/,*):")
	num2 = input("Digite o segundo número:")
	num2 = int(num2)

	# SOMA:
	if ope == "+":
		operacao = num1 + num2
	# subtração
	if ope == "-":
		operacao = num1 - num2
	#divisão
	if ope == "/":
		operacao = num1 / num2
	#multiplição
	if ope == "*":
		operacao = num1 * num2


	print("Resultado:")
	print(operacao)

	test = input ("Deseja sair ? (n/s):")
	if test == "s":
		sair = True
