# Faça um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra A.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip().lower()

print('A letra "A" aparece',frase.count('a'), 'vezes.')

print('A letra "A" aparece pela primeira vez no',frase.find('a'), 'º espaço.')

print('A letra "A" aparece por último no',frase.rfind('a'), 'º espaço.')