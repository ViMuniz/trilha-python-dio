#Operação mátematica de intersecção, onde os valors em comum dos conjuntos são destacados
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_C = {0, 5, 3}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

resultado_01 = conjunto_a.intersection(conjunto_b, conjunto_C)
print(resultado_01)