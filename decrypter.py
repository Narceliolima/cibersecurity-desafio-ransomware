import os
import pyaes
import sys

# Verificar se o nome do arquivo foi passado como argumento
if len(sys.argv) != 2:
    print("Uso: python decrypter.py <nome_do_arquivo>")
    sys.exit(1)

# Obter o nome do arquivo do argumento de linha de comando
file_name = sys.argv[1]

## abrir o arquivo a ser criptografado
# Abrir, ler e fechar o arquivo
try:
    with open(file_name, "rb") as file:
        file_data = file.read()
        file.close()
    print("Arquivo lido com sucesso!")
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
