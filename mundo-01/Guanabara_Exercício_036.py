'''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
cores = {
    'semcor': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
}

# Header
print(f'{cores['verde']}=-={cores['semcor']}'*18)
print('PROGRAMA PARA AVALIAR APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO')
print(f'{cores['verde']}=-={cores['semcor']}'*18)

# Entradas e tratamento de erros
while True:
    casaValor = float(input('Valor do imóvel: R$'))
    compradorSalario = float(input('Salário do comprador: R$'))
    anosQuitar = int(input('Total de anos do empréstimo: '))
    if casaValor != 0 and compradorSalario != 0 and anosQuitar != 0:
        break
    else:
        print(f'{cores['vermelho']}Digite apenas valores válidos.{cores["semcor"]}')

# Cálculo
prestacaoMensal = casaValor / (anosQuitar*12)
salario_30Porcento = compradorSalario * 30/100

# Condicionais e Outputs
print(f'A prestação de uma casa no valor de {cores['verde']}R${casaValor:.2f}{cores["semcor"]} para um comprador que ganha um salário de {cores['verde']}R${compradorSalario:.2f}{cores["semcor"]}, fica no valor de {cores['verde']}R${prestacaoMensal:.2f}{cores["semcor"]}.')
if prestacaoMensal > salario_30Porcento:
    print(f'{cores['vermelho']}Empréstimo negado.{cores['semcor']}')
else: 
    print(f'{cores['verde']}Empréstimo bem sucedido.{cores['semcor']}')

