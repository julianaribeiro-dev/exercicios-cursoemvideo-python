'''
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

carVel = int(input('Velocidade do carro (em km/h)): '))

carTicket = (carVel-80)*7

if carVel > 80:
    print('Você foi multado.')
    print(f'Valor da multa: R${carTicket:.2f}')
else:
    print('Carro em velocidade normal.')