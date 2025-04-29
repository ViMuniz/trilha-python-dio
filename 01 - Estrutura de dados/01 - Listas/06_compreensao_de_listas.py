# DETALHAMENTO
# pares = [numero for numero in numeros if numero % 2 == 0]
#
# pares = lista em que será salvo os valores
# numero = é o retorno, o que compo~em a lista pares
# for numero in numeros = interação de retorno o valor em numero analisando a lista numeros
# Primeiro argumento é o retorno da condição de interação entre a variavel numero e a lista numeros
#avaliando a condição do IF e se for verdadeira o numero é armazenado na lista pares[]

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] # 
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

#Outra forma de achar os números pares porém não é vantajosa, pois a instrução é mais longa
pares01 = []

for numero in numeros:
    if numero % 2 == 0:
        pares01.append(numero) #Adiciona valores na lista
print(pares01)

