# Crie um script que:
# - Leia nomes.txt
# - Para cada nome, imprima: "Nome: [nome]"

with open("nomes.txt", "r") as file:
    for nome in file:
        print(f'Nome: [{nome.strip()}]')