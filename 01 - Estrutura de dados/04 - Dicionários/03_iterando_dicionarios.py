contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Não é o melhor método para se aplicar
for chave in contatos:
    print(chave, contatos[chave]) # A chave retorna os emails que está amarrada com as demais informações
    
print(chave)
print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)
