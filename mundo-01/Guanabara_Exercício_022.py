frase = str(input('Digite uma frase: ')).strip()

# Colocando a frase toda em maiúsculo e minúsculo.
print('Seu nome em maiúsculo é:', frase.upper())
print('Seu nome em minúsculo é:', frase.lower())

# Quantidade de letras em toda a string excluindo os espaços entre as palavras.
no_spaces = frase.split()
qtd_letras = "".join(no_spaces)

print('A frase tem:',len(qtd_letras), 'letras.')

# Identificando quantas letras tem a primeira palavra.
print('A primeira palavra tem:',len(no_spaces[0]), 'letras.')