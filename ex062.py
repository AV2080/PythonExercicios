print('Gerador de P.A')
print('=-' *10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='') # ALT = 26
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Progressão finalizada com {} termos mostrados'.format(total))