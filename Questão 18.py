#Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.

numeros = input('Digite alguns números, separados por espaço: ')
lista = numeros.split()

#inicio da multiplicação
mult = 1
for num in lista:
   mult *= int(num)

print('O produto dos números é:', mult)