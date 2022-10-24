from cryptography.frenet import Fernet

key = Fernet.generate_key()

#write
with open ('filekey.key', 'wb') as filekey:
    filekey.write(key)

#read
with open ('filekey.key', 'rb') as filekey:
    key = filekey.red()

fernet = Fernet(key)
 with open ('test.txt', 'rb') as file:
     original = file.read()

encrypted = fernet.encrypted(original)

with open('test.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

