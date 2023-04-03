#Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num) #append serve para adicionar os números inseridos na lista

menor5 = [] #armazena os números 
for n in lista:
    if n < 5:
        menor5.append(n)

if menor5: #mostra o resultado
    print('Os números maiores que 10 são:', end=' ')
    for num in menor5:
        print(num, end=' ')