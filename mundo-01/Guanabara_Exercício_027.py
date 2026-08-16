# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = input('Digite seu nome: ').strip().split()

print('Primeiro: ',nome[0])
print('Último: ',nome[-1])
