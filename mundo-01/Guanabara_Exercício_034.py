'''
Escreva um programa que pergunte o salário de um funcionário.
Calcule o valor do seu aumento.

Para salários superiores a R$1250, calcule um aumento de 10%.
Para salário inferiores ou iguais, calcule um aumento de 15%.
'''

salario = float(input('Salário: '))

if salario <= 1250:
    aumento = (salario*15/100) + salario
    print(aumento)
else:
    aumento = (salario*10/100) + salario
    print(aumento)
