# Tem sempre valores únicos e a chave deve ter sempre um valor
pessoa = {"nome": "Vinicius", "idade": 25}
print(pessoa)

pessoa = {"nome": "Vinicius", "idade": 25, "nome": "Muniz"}
print(pessoa)

pessoa = dict(nome="Vinicius", idade=25)
print(pessoa)

#Adiciona uma nova chave no dicionário
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

#Adiciona chave já existente e o sistema reescreve o valor
pessoa["nome"] = "Muniz"
print(pessoa)