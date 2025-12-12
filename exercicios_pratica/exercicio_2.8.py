# Crie um script que:
# - Leia nomes.txt
# - Conte quantos nomes começam com cada letra
# - Imprima: "Letra A: 2 nomes"

# Dicas:

# Loop em cada nome
# Use .startswith() pra verificar primeira letra
# Use dicionário pra contar por letra? Ou if?

# Exemplo:
# pythonnome = "João"
# nome[0]           # "J"
# nome.upper()      # "JOÃO"
# nome.startswith("J")  # True

with open("nomes.txt", "r") as file:
    contagem = {}
    for nome in file:
        nome = nome.strip()
        #pega primeira letra
        primeira_letra = nome[0]

        if primeira_letra not in contagem:
            contagem[primeira_letra] = 1
        else:
            contagem[primeira_letra] += 1

for letra in contagem:
    print(f"Letra {letra}: {contagem[letra]} nomes")

