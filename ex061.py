print('Gerador de P.A')
print('=-' *10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='') # ALT = 26
    termo += razão
    cont += 1
print('FIM')
