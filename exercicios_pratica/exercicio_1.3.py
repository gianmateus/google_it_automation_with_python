# Crie um script que:
# - Abra teste.txt em modo append
# - Adicione uma nova linha: "Linha 2"
# - Mostre o arquivo inteiro

with open('teste.txt', 'a') as file:
    conteudo = file.write('\nLinha 2')

with open('teste.txt', 'r') as file:
    conteudo = file.read()
print(conteudo)