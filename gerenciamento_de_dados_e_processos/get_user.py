import subprocess
import sys

comando = ["whoami"]

print("--- Executando o subprocesso whoami ---")

try:
    resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
    username_limpo = resultado.stdout.strip()
    print(f"Nome de Usuário Capturado: {username_limpo}")
    print(f"Tipo de dado: {type(username_limpo)}")
    print(f"O comando Whoami teve sucesso? {'Sim' if resultado.returncode == 0 else 'Não'}")

except subprocess.CalledProcessError as e:
    # Se o comando falhar, o check=True levantará esta exceção
    print(f"Erro ao executar o comando: {e}")
    sys.exit(1)
except FileNotFoundError:
    # Captura o erro se o executável 'whoami' não for encontrado no PATH
    print("ERRO: O comando 'whoami' não foi encontrado. Verifique seu PATH.")
    sys.exit(1)