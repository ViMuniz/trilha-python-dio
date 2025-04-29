# Mescla uma lista dentro de outra mas cria com coordenadas individuais e não como uma lista 
#dentro de lista
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp", "c"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
