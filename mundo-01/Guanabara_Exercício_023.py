# Faça um programa que leia um número de 0 a 9999 e mostre cada um dos digitos separados.
'''
Ex: Digite um número: 1834
    Unidade: 4
    Dezena: 3
    Centena: 8
    Milhar: 1
'''

import random

# Ao invés de pedir ao usuário automatizei para já mostrar um número entre o range proposto.
numero = random.randint(0,9999)
print(numero)
# Transformando o integer em string e preenchendo os espaços vazios caso var numero < 1000.
numero = str(numero).zfill(4)

print('Unidade:',numero[3])
print('Dezena:',numero[2])
print('Centena:',numero[1])
print('Milhar:',numero[0])

'''
Também rola fazer assim:

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Unidade:',unidade)
print('Dezena:',dezena)
print('Centena:',centena)
print('Milhar:',milhar)

'''