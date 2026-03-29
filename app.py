from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            name, password = data.split("|")
            decrypted_password = fer.decrypt(password.encode()).decode()
            print(f"Name: {name} | Password: {decrypted_password}")
            print("----------------------------------------------")

while True:
    mode = input("would you like to view password or create a new one?"
    "(view/add) or click quit to end the program: ").lower()  
    if mode == "quit":
        print("See you soon!")
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue
