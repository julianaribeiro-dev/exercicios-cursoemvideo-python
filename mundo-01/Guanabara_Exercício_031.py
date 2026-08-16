'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km.
E R$ 0,45 para viagens mais longas.
'''

viagemKm = float(input('Distância da viagem em Km: '))

if viagemKm <= 200:
    print(f'O valor da passagem é: {viagemKm*0.5}')
else:
    print(f'O valor da passagem é: {viagemKm*0.45}')