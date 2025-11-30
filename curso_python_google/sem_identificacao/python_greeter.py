# greeter.py
import sys

# A lista sys.argv sempre terá pelo menos 1 elemento (o nome do script)
# Se o tamanho for 1, significa que nenhum argumento adicional foi passado.
if len(sys.argv) == 1:
    print("ERRO: Você deve fornecer um nome como argumento!")
    print("Uso correto: python {sys.argv[0]} <nome>")
    # Retornamos um Exit Status de 1 (falha)
    sys.exit(1)

# Se chegamos aqui, sabemos que há pelo menos um nome.
# sys.argv[0] é o nome do script
# sys.argv[1] é o primeiro argumento (o nome que queremos)

nome_principal = sys.argv[1]
num_args = len(sys.argv) - 1 # Excluímos o nome do script

print("-" * 30)
print(f"Saudações, {nome_principal}!")

if num_args > 1:
    print(f"OBS: Você passou mais de um argumento ({num_args} no total).")
    print("Todos os argumentos passados foram:")
    # sys.argv[1:] pega todos os elementos da lista a partir do índice 1
    print(sys.argv[1:])
    
print("-" * 30)
# Se o script terminar normalmente, ele implicitamente retorna um Exit Status de 0 (Sucesso)