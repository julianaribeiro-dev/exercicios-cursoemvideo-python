'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
Peça para o usuário tentar descobrir qual foi o número.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep

num = random.randint(0,5)

print('-=-'*20)
print('Adivinhe qual foi o número que eu escolhi de 0 a 5.')
print('-=-'*20)

numSelected = int(input('\nNúmero escolhido: '))

print('\nPROCESSANDO...')
sleep(3)

if numSelected != num:
    print('\nNúmero errado. Você perdeu!')
    print(f'O número correto era: {num}')
else:
    print('\nNúmero correto! Parabéns!')