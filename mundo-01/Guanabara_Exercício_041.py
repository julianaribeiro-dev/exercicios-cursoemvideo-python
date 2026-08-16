'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

Até 9 anos: MIRIM

Até 14 anos: INFANTIL

Até 19 anos: JÚNIOR

Até 25 anos: SÊNIOR

Acima de 25 anos: MASTER

'''
from datetime import datetime

nasc = int(input('Ano de nascimento: '))
x = (datetime.now().year - nasc)
print(x)

if x <= 9:
    print('Categoria: MIRIM')
elif x <= 14:
    print('Categoria: INFANTIL')
elif x <= 19:
    print('Categoria: JÚNIOR')
elif x <= 25:
    print('Categoria: SÊNIOR')
elif x > 25:
    print('Categoria: MASTER')

'''
FALTA TESTAR SE TÁ TUDO CERTO!!!!!!!!!!!!!!!!!!!
'''