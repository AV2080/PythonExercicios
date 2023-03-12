real = float(input('Quanto dinheiro você tem na carteira? R$ '))
#Cotação do dia 26/02/2023
dolar = real / 5.21
euro = real / 5.50
iene = real / 0.04
print('Com R${:.2f} você pode comprar US${:.2f} ou E${:.2f} ou Y${:.2f}'.format(real, dolar, euro, iene))
