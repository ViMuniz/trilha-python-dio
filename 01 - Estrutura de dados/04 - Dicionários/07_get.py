#Usado para quando não se sabe o nome da chave e se o ID não for igual o programa não é pausado, 
# apenas retona o valor Null

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

#contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {} se não encontra a chave e se não encontrar retona o que estiver depois da ","
print(resultado)

resultado = contatos.get("guilherme@gmail.com").get("telefone")
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
