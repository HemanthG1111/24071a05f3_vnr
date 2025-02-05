import random
import string

def generate_password(length=10):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = [ #atleast 1 character
        random.choice(string.ascii_lowercase), 
        random.choice(string.ascii_uppercase), 
        random.choice(string.digits), 
        random.choice(string.punctuation)
    ]
    
    password += random.choices(all_characters, k=length - 4) #rest random characters
    
    random.shuffle(password) #shuffle
    
    return ''.join(password) #converting to string from list


password = generate_password(10)
print(password)