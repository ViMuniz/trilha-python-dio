carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

print("\n")

# O enumerate retorna 2 valores, o indice e o item
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
