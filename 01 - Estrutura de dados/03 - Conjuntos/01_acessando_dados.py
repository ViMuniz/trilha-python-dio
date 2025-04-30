#Para acessar o dado de um conjunto é necessário transform-lo em lista
numeros = {1, 2, 3, 2}
# print(numeros[3]) ocorre erro

numeros = list(numeros)
print(numeros[2])
