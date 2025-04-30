# Usado para criar chaves em duas situações: 1° Criar chaves mas não vincular valor; 2º Cria chaves e define valor padrão
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)