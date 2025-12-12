# Crie um script que:
# - Peça 5 nomes ao usuário
# - Salve em arquivo usuarios.txt
# - Leia o arquivo
# - Conte quantas linhas tem
# - Imprima: "Total de usuários: [número]"

with open("usuarios.txt", "w") as file:
    for i in range(5):
        nome = input("Digite o nome de um usuário: ")
        file.write(nome + "\n")

with open("usuarios.txt", "r") as file:
    conteudo = file.readlines()
    quantidade_de_linhas = len(conteudo)
print(f"Total de usuários: {quantidade_de_linhas}")
