get_number = int(input('Digite um número: '))
max_number = 10

if get_number > max_number:
  print(f'{get_number} é maior que {max_number}')
elif get_number == max_number:
  print(f'{get_number} é igual que {max_number}')
else:
  print(f'{get_number} é menor que {max_number}')