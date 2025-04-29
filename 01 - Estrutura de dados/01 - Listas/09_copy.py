lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(l2)

lista.append("Teste de copy")
print("----------------------")
print(lista)  # [1, "Python", [40, 30, 20], "Teste de copy"]
print(l2) # [1, "Python", [40, 30, 20]]

l2[0] = 7
print("----------------------")
print(lista)  
print(l2) 