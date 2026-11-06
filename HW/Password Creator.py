import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']  
digits = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9'] 
special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')','*', '+', ',', '-', '.', '/', ':', ';', '<','=', '>', '?', '@', '[', ']', '^', '_','`', '{', '|', '}', '~'] 
w = ""  
for i in range(5):  
    w += random.choice(letters) + random.choice(digits) + random.choice(special_characters) 
print(w) 
