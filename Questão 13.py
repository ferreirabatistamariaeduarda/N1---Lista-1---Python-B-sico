#Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".

palavras = input('Escreva algumas palavras separadas por espaços: ')
lista = palavras.split()

print('As palavras que começam com A são: ')
for plvr in lista:

#.lower() verifica se as letras estão em maiusculas e as converte em minusculas
#.startswith() 
    if plvr.lower().startswith('a'):
        print(plvr)
    else: 
        print('Nenhuma das palavras começa com a letra: A')