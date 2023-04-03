#Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa.

palavra = str(input('Digite as palavras, separadas por vírgulas ou espaços: '))

#separa as palavras digitadas
lista = palavra.split()

#inicia a lista vazia
plonga = []

#loop
for i in lista:
    if len(i) > len(plonga):
        plonga = i

#len -- serve para a contagem de caracteres no string

print('A palavra mais longa é: ', plonga)

