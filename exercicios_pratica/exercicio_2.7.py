# Crie um script que:
# - Peça 3 cidades ao usuário
# - Salve cada uma em linha diferente em cidades.txt
# - Leia o arquivo
# - Imprima: "Cidades registradas:" seguido de cada cidade

with open("cidades.txt", "w") as file:
    for i in range(3):
        cidade = input("Digite uma cidade: ")
        file.write(cidade + "\n")

with open("cidades.txt", "r") as file:
    print("Cidades registradas: ")
    for city in file:
        print(city.strip())
