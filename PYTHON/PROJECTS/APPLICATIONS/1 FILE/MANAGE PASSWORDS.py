from cryptography.fernet import Fernet 

'''
key + password + text to encrypt = random text 
random text + key + password = text to encrypt
if you type the wrong master password + key -> wrong decrypted text 
'''
'''def write_key():
    key = Fernet.generate_key()
        # 'wb': write bytes mode 
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key() 
    # convert ther master pass into bytes to be compatible 
fer = Fernet(key)


   # put these before the loop 
# define 'view' function 
def view(): 
    with open('password.txt', 'r') as f: 
        for line in f.readlines():
            # rstrip(): strip off the carriage return from our line 
            # data = line.rstrip()
            user, passw = line.rstrip()
            user, passw = line.split('|')
            # this will automatically assign the order for the variables -> user is first, passw is second 
            print('User: ', user, '| Password: ', fer.decrypt(passw.encode()))

'''
b'hello': a BYTES STRING
'hello': a normal string 
'''

# define 'add' function 
def add():
    acc_name = input ('Account name: ')
    pss = input ('Password: ')

        # a new file will be created 
        # 'a' is mode 'append' values at the end of the file 
        # 'with' will automatically closed for us instead of manually 
    with open('password.txt', 'a') as f: 
        f.write(acc_name + "|" + fer.encrypt(pss.encode()).decode())
    print('Password added succesfully!')


# 'Main' code 
while True: 
    mod  = input ('Would you like to add a new password or view existing ones? Press q to quit.').lower()

    if mod == 'q': 
        break
    if  mod == 'view': 
        view()
    elif mod == 'add':
        add()

    else: 
        print('Invalid mode!')
        continue 