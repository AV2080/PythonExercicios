from math import hypot
co = float(input('Comprimento do cateoto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
