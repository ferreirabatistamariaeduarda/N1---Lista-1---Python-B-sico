#Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num) #append serve para adicionar os números inseridos na lista
    
print('Os números ímpares são: ')    
for num in lista:
    if num % 2 != 0:
        print(num, end=' ')