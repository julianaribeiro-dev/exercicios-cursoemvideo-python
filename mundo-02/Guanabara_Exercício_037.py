'''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal.
'''
print('CONVERSÃO DE BASES: BINÁRIO, OCTAL E HEXADECIMAL')
num = int(input('Digite um número inteiro: '))

base_de_conversao = int(input('''Escolha uma das bases para conversão:
[ 1 ] Binário \
[ 2 ] Octal \
[ 3 ] Hexadecimal\n'''))

if base_de_conversao == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif base_de_conversao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif base_de_conversao == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
