# Crie um programa que leia a cidade em que você mora e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: '))

maiusc = cidade.upper().split()

teste = 'SANTO'.find(maiusc[0])

if teste == -1:
    print('Não começa com SANTO.')
else:
    print('Começa com SANTO.')
