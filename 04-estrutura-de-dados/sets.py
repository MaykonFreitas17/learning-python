# Sets ou Conjuntos

# Sintaxes = conjunto1 =  { valor1, valor2, valorN }
# Sintaxes = conjunto2 =  set([valor1, valor2, valorN])

users1 = { "Maykon Freitas", "Bruno Sousa", "Tharcio Andrades", "Guilherme Augusto" }
users2 = set(["Rafael Lima", "Maykon Freitas", "Patricia Santiago", "Diogo Oliveira"])

print(users1)
print(users2)

# Adicionando um novo valor ao conjunto - add(valor)
users1.add("Samuel Pinheiro") # Adicionando o valor Samuel Pinheiro no conjunto
print(users1)

# Conjuntos não podem possuir valores igual
users1.add("Samuel Pinheiro") # Adicionando o valor Samuel Pinheiro no conjunto
print(users1) # Ao imprimir o conjunto, vemos que não possui dois valores com Samuel Pinheiro, apenas uma ocorrencia.

""" Operações com Conjuntos """

# União entre dois conjuntos - union(conjunto)
print(users1.union(users2))
print(users1 | users2) # Outra maneira de fazer uma união entre dois conjuntos 

# Interseção entre dois conjuntos - intersection(conjunto)
print(users1.intersection(users2))
print(users1 & users2) # Outra maneira de fazer a interseção entre dois conjuntos

# Diferença entre dois conjuntos - difference(conjunto)
print(users1.difference(users2))
print(users1 - users2) # Outra maneira de fazer a diferença entre dois conjuntos