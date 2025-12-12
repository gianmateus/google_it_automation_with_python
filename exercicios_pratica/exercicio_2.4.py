# Crie um script que:
# - Peça ao usuário um nome
# - Salve em arquivo dados.txt
# - Leia o arquivo
# - Imprima: "O nome salvo foi: [nome]"

with open("dados.txt", "a") as file:
    nome = input("Digite um nome: ")
    file.write(nome + "\n")

with open("dados.txt", "r") as file:
    conteudo = file.read()

print(f'O nome salvo foi: {conteudo.strip()}')