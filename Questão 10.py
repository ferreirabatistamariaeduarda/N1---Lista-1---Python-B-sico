#Crie um programa que leia uma lista de números do usuário e exiba a média desses números.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num)

#inicio
soma = 0
for i in lista:
    soma += i

#len serve para contar os caracteres dentro do vetor ou da string
média = soma / len(lista)

print('A média entre os números digitados é: ', média)
