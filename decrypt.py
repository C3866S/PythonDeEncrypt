from tkinter import Tk     
from tkinter.filedialog import askopenfilename

Tk().withdraw()  
filename = askopenfilename() 
print(filename)


import pyAesCrypt
password = input()
#decrypt 

pyAesCrypt.decryptFile(filename, filename +"out" +".txt", password)
