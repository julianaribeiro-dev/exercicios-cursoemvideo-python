'''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import datetime

sexo = input('Digite seu sexo: ').lower().strip()

if sexo == 'feminino':
    print('Você não precisa fazer o alistamento obrigatório.')
    quit()

elif sexo == 'masculino':
    ano_nascimento = int(input('Digite o ano de nascimento: '))

    ano_atual = datetime.now().year
    idade_atual = ano_atual - ano_nascimento
    alistamento = idade_atual - 18
    
    if alistamento < 0:
        print(f'Você poderá se alistar daqui há {abs(alistamento)} anos.')
    elif alistamento > 0:
        print(f'Já passou {alistamento} anos do seu período de alistamento.')
    else:
        print('Está na hora de se alistar!')
