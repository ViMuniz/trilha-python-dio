# Estruturas dentro de outras estruturas define dicionários aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "vinicius@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a":1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

dados_cliente = contatos["chappie@gmail.com"]
print(dados_cliente)

dados_cliente = contatos["giovanna@gmail.com"]["nome"]
print(dados_cliente)


dados_cliente = contatos["vinicius@gmail.com"]["extra"]["a"]
print(dados_cliente)