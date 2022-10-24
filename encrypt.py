from tkinter import Tk     
from tkinter.filedialog import askopenfilename

Tk().withdraw()  
filename = askopenfilename() 
print(filename)

#Encryptiom
import pyAesCrypt

password = input()
pyAesCrypt.encryptFile( filename, filename + ".aes", password)
