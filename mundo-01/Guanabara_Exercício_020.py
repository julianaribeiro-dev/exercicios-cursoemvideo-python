import random

print('Sorteio ordem de apresentação dos trabalhos: \n')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome de o terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista_alunos = [a1, a2, a3, a4]
print(random.sample(lista_alunos, k=4))
