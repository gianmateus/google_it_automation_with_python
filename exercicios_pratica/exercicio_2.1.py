# Crie um script que:
# - Peça 3 nomes ao usuário
# - Salve cada nome em uma linha do arquivo nomes.txt

with open("nomes.txt", "a") as file:
    for i in range(3):
        nome = input("Digite um nome: ")
        file.write(nome + "\n")