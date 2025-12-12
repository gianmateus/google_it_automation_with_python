# Crie um script que:
# - Leia nomes.txt
# - Imprima cada nome com número:
#   "1. João"
#   "2. Maria"
#   etc

with open("nomes.txt", "r")as file:
    for i, nome in enumerate(file, 1):
        print(f'{i}. {nome.strip()}')
        