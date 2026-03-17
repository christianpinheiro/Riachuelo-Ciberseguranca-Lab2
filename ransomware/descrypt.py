from cryptography.fernet import Fernet
import os

with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

folder = "test_files"

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if os.path.isfile(path):

        with open(path, "rb") as f:
            encrypted_data = f.read()

        decrypted = fernet.decrypt(encrypted_data)

        with open(path, "wb") as f:
            f.write(decrypted)

print("Arquivos restaurados!")
