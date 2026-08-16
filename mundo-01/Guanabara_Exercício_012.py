import math

preco_produto = float(input('Preço do produto: R$'))
desconto = preco_produto * 5/100
preco_produto_desconto5 = preco_produto - desconto
print(f'O produto que custava R${preco_produto:.2f}, teve R${desconto:.2f} de desconto na promoção de 5%, com valor final de R${preco_produto_desconto5:.2f}')
