

largura = float(input('Largura da parede (em metros): '))
altura = float(input('Altura da parede (em metros): '))
area = (altura * largura)

'''Cada litro de tinta pinta uma parede de area de 2 m²'''

print(f'A parede tem as dimensões {largura} m x {altura} m e sua área é de {area:.2f} m²')
print(f'A quantidade de tinta necessária para pintar {area:.2f} m² de parede é: {area/2:.2f} litros')