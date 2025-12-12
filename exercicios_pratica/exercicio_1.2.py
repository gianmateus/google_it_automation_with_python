# Crie um script que:
# - Abra teste.txt
# - Leia o conteúdo
# - Imprima na tela

with open('teste.txt', 'r') as file:
    conteudo = file.read()
print(conteudo)