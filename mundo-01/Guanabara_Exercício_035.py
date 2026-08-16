'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if r1 >= r2 and r1 >= r3:
    if r2 + r3 > r1:
        print('Pode formar um triângulo.')
    else:
        print('Não é possível formar um triângulo.')
elif r2 >= r1 and r2 >= r3:
    if r1 + r3 > r2:
        print('Pode formar um triângulo.')
    else:
        print('Não é possível formar um triângulo.')
elif r3 >= r1 and r3 >= r2:
    if r1 + r2 > r3:
        print('Pode formar um triângulo.')
    else:
        print('Não é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')


