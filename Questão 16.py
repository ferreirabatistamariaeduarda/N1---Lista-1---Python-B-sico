#Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.

quant = int(input('insira a quantidade de números na lista: '))
lista = []

for i in range(quant):
    num = int(input('Digite um número: '))
    lista.append(num)

#inicio da soma
soma = 0
for num in lista:
    if int(num) % 2 == 0:
        print('Número par encontrado:', num)
        soma += int(num)

print('A soma dos números pares é:', soma)


  
