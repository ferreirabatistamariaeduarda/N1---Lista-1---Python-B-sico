#Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.

num = int(input('Digite um número: '))

if num %2 == 0:
    print('Este número é par')
if num %2 != 0:
    print('Este número é ímpar')

