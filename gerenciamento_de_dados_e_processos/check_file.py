import subprocess
import sys

NOME_ARQUIVO = "arquivo_inexistente.txt"

comando = ["dir", NOME_ARQUIVO]

print(f"Tentando executar comando do sistema: {' '.join(comando)}")

resultado = subprocess.run(comando, capture_output=True, shell = True)

if resultado.returncode != 0:
    print("-" * 40)
    print("DIAGNOSTICO: O SUBPROCESSO FALHOU!")
    print(f"Mensagem de erro (STDERR): {resultado.stderr.decode()}")
    print(f"Código de retorno (exit status): {resultado.returncode}")
    print("Ação: O script Python faria um LOG ou tentaria um comando alternativo.")
    print("-" * 40)
    sys.exit(1)
else:
    print(f"O arquivo {NOME_ARQUIVO} existe no sistema.")
    sys.exit(0)