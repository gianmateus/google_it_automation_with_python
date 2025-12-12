# # Crie um script com 2 funções:
# # - ler_vendas(arquivo)
# #   Abre arquivo CSV com vendas
# #   Retorna: lista de dicionários
import csv

def ler_vendas(arquivo):
    with open(arquivo, "r") as file:
        reader = csv.DictReader(file)
        vendas = [dict(row) for row in reader]
        return vendas


# #
# # - contar_por_vendedor(vendas)
# #   Recebe: lista de dicionários
# #   Retorna: dicionário com vendedor: quantidade

def contar_por_vendedor(vendas):
    contagem = {}
    for venda in vendas:
        vendedor = venda["vendedor"]
        if vendedor not in contagem:
            contagem[vendedor] = 1
        else: 
            contagem[vendedor] += 1
    return contagem

# #
# # Depois use para:
# # - Ler arquivo vendas.csv (já existe)
# # - Contar vendas por vendedor
# # - Imprimir: "Vendedor: X vendas"
# ```

vendas = ler_vendas("vendas.csv")
resultado = contar_por_vendedor(vendas)
for vendedor, quantidade in resultado.items():
    print(f"{vendedor}: {quantidade} vendas")
# ---

# ## **Arquivo vendas.csv (crie antes):**
# ```
# vendedor,produto,valor
# João,Notebook,5000
# Maria,Mouse,50
# João,Teclado,200
# Pedro,Monitor,1500
# Maria,Headset,300
# João,Mousepad,30