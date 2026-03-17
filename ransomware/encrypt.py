from cryptography.fernet import Fernet
import os

# gera chave
key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

# pasta com arquivos de teste
folder = "test_files"

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):

        with open(path, "rb") as f:
            data = f.read()

        encrypted = fernet.encrypt(data)

        with open(path, "wb") as f:
            f.write(encrypted)

print("Arquivos criptografados!")
