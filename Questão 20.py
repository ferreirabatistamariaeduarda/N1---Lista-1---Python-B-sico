#Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num)
    
    #ordem crescente
    lista.sort()
    lista.reverse() #reverte a ordem
    
print('A lista ordenada é:', lista)


