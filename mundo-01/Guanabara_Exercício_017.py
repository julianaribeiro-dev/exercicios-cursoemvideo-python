import math

cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(cat_oposto, cat_adj)
print(f'O valor da hipotenusa é {hipo:.2f}')