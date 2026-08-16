salario_antigo = float(input('Insira o valor do salário atual: R$')) 
salario_novo = salario_antigo + (salario_antigo * 15/100)
print(f'\nUm funcionário que ganhava R${salario_antigo:.2f} reais, com o reajuste de 15%, passa a receber R${salario_novo:.2f} reais.')
print(f'Sendo assim, obteve um aumento de R${salario_antigo*15/100:.2f} reais.')