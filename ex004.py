a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Éstá em maiuscular? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())