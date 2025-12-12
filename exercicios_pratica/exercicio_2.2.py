# Crie um script que:
# - Leia nomes.txt
# - Conte quantas linhas tem
# - Imprima o total

with open("nomes.txt", "r") as file:
    linhas = file.readlines()
    quantidade_de_linhas = len(linhas)
print(quantidade_de_linhas)