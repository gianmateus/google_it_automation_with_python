# Crie 2 funções:
# - contar_linhas(arquivo)
#   Recebe: nome do arquivo
#   Retorna: número de linhas

def contar_linhas(arquivo):
    with open(arquivo, "r") as file:
        linhas = file.readlines()
        numero_de_linhas = len(linhas)
        return numero_de_linhas

# - listar_linhas(arquivo)
#   Recebe: nome do arquivo
#   Retorna: lista com cada linha

def listar_linhas(arquivo):
    with open(arquivo, "r") as file:
        lista_linhas = file.readlines()
        lista_limpa = [linha.strip() for linha in lista_linhas]
        return lista_limpa

#
# Depois use as funções para:
# - Ler nomes.txt
# - Contar quantas linhas tem
# - Listar todas as linhas
# - Imprimir:
#   "Total de linhas: [número]"
#   Linha 1: [nome]
#   Linha 2: [nome]
#   etc

total = contar_linhas("nomes.txt")
print(f"O total de linhas é: [{total}]")
listar_todas_as_linhas = listar_linhas("nomes.txt")
for i, linha in enumerate(listar_todas_as_linhas, 1):
    print(f"Linha {i}: {linha}")


# Dicas:
# Função 1: contar_linhas(arquivo)
# Pense:

# Abre arquivo em modo 'r'
# Usa .readlines() (retorna lista)
# Conta com len()
# Retorna o número


# Função 2: listar_linhas(arquivo)
# Pense:

# Abre arquivo em modo 'r'
# Usa .readlines() (retorna lista)
# Retorna a lista (sem \n!)


# Usar as funções:
# python# Pega número de linhas
# total = contar_linhas("nomes.txt")
# print(f"Total de linhas: {total}")

# # Pega lista de linhas
# linhas = listar_linhas("nomes.txt")
# for i, linha in enumerate(linhas, 1):
#     print(f"Linha {i}: {linha.strip()}")



    
