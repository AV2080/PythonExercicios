distância = float(input('Qual é a distância da sua viagem? '))
print('Você está preses a começar uma viagem de {}Km.'.format(distância))
'''
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço de sua passagem será de {:.2f}R$.'.format(preço))