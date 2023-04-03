#Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.

num = int(input('Digite a quantidade de números que irão ser inseridos: '))

#inicia a lista vazia
nums = []

#pede pra inserir os números
for i in range(num):
    #pede pra digitar um por um
    n = int(input('Digite o {}ª número: '.format(i+1)))
    nums.append(n)
    #função para adição
    soma = sum(nums)
    print('A soma é:', soma)





