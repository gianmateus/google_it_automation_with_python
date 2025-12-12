# Crie 2 funções:
# - salvar_dados(arquivo, dados) 
#   Recebe: nome do arquivo e texto
#   Faz: salva o texto no arquivo
#
# - ler_dados(arquivo)
#   Recebe: nome do arquivo
#   Retorna: conteúdo do arquivo
#
# Depois use as funções para:
# - Pedir um texto ao usuário
# - Salvar em arquivo.txt
# - Ler do arquivo.txt
# - Imprimir: "Dados salvos: [conteúdo]"

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as file:
        file.write(dados)

def ler_dados(arquivo):
    with open(arquivo, 'r') as file:
        return file.read()

texto = input("Digite o texto a ser salvo: ")
salvar_dados("arquivo.txt", texto)
print(ler_dados("arquivo.txt"))
