# Crie um programa que leia o nome de uma pessoa e diga se o nome tem "SILVA".

# Entrada do nome com tratamento de string.
nome = str(input('Digite seu nome: ')).upper().strip()

analise_silva = nome.count("SILVA")

if analise_silva.strip() > 0:
    print('O nome tem "Silva"!')
else:
    print('O nome não tem "Silva"!')