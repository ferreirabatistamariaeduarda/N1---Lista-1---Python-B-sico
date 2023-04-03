#Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num)

maior = lista [0] #inicia a lista
#loop
for n in lista:
    if n > maior:
        maior = n

print('O maior número é: ', maior)
