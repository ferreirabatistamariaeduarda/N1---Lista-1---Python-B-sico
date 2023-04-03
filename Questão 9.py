#Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista.
quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num)

menor = lista [0] #inicia a lista
#loop
for n in lista:
    if n < menor:
        menor = n

print('O maior número é: ', menor)
