print("Welcome World of python")

#Este e meu comentario otario.

'''se

e

loko '''

print("Ulla lá")

nome = "rafael"

print('Ola ' + nome)

#Entrada de dados pelo terminal. Por padrão toda entrada é String
nome = input("Digite seu nome: ")
print(nome + " bem vindo ao sistema! ")

#Quando trabalhamos com números. temos que converter a variavel
idade = input("Digite sua idade!")
idade = int(idade)
#idade = float(idade)

'''
Operades

+
-
/
*

** É usado para calcular Potência

2**3 = 8
8**2 =64

A raiz quadrada de um número é ele elevado a (1x)

16**(1/2) - raiz quadrada de 16
16**(1/3) - raiz cúbica de 16
257**(1/5) - raiz de grau 5

'''
print("Á raiz é ", 16**(1/4))

'''

Condicionais

'''

a = 20

if a > 10 :
    print(a , "é maior que 10.")

elif a < 10 :
    print(a , "é menor que 10.")

else:
    print(a , "é igual a 10.")

'''
Laço de repetição WHILE

'''

x = 1
t = 8

while x <= 10:
    print(x , "x", t, "=", t*x)

    x += 1

print("Terminol aqui o While")
