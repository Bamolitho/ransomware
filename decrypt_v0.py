#!/usr/bin/python

import os
from cryptography.fernet import Fernet

# Take the stored key in the file
with open("my_key.key", "rb") as file_key:
   my_key = file_key.read()

# Stocker le nom des fichiers à déchiffrer
files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "my_key.key" or file == "decrypt.py":
        continue
    files.append(file)

# Chiffrer les fichiers
for file in files:

    # Read the content of the file
    with open(file, "rb") as file2decrypt:
        file_content= file2decrypt.read() # Encrypt the content
    file_content_decrypted = Fernet(my_key).decrypt(file_content)

    # Put the decrypted content in the file
    with open(file, "wb") as to_encrypt:
        to_encrypt.write(file_content_decrypted)

