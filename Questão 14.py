#Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num) #append serve para adicionar os números inseridos na lista

maior10 = [] #armazena os números 
for n in lista:
    if n > 10:
        maior10.append(n)

if maior10: #mostra o resultado
    print('Os números maiores que 10 são:', end=' ')
    for num in maior10:
        print(num, end=' ')