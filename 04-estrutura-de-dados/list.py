# Sintaxe = nome_lista = [valor01, valor2, valor3, valorN]
number_list = [8, 10, 6.5, 9]
name_list = ["Maria", "João", "Marcos", "Pedro"]
print(number_list)
print(name_list)

# Pegando valores da list pelo index
print(number_list[0]) # index 0 representa o primeiro valor da lista, no caso, 8
print(name_list[1]) # pegando o segundo valor da lista -> João

""" Funções relacionadas as lists"""

# Adicionando um novo valor a lista - append
number_list.append(10) # Adicionando o valor 10 no final da lista
print(number_list)

# Ordenando lista - sort
number_list.sort() # Ordenando a lista de número de forma crescente
print(number_list)
number_list.sort(reverse=True) # Ordenando a lista de número de forma decrescente
print(number_list)

name_list.sort() # Ordenando a lista de nomes (Strings) de forma Alfabetica
print(name_list)
name_list.sort(reverse=True) # Ordenando a lista de nomes (Strings) de forma Alfabetica descrescente
print(name_list)


# Removendo o último elemento da List - pop
name_list.pop() # Remove e Retorna o ultimo elemento da lista
print(name_list)

# Adicionando um novo valor na lista em uma posição definida - insert(index, valor)
name_list.insert(3, "João") # Inserindo o valor João na posição 3 (No final da lista)
print(name_list)

# Removendo um elemento pelo o seu index - pop(index)
name_list.pop(3) # Remove e Retorna o ultimo elemento da lista
print(name_list)