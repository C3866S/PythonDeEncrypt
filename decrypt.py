

fernet = Fernet (key)

with open ('test.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open ('test.txt', 'wb') as dec_file 
    dec_file.write(decrypted)
