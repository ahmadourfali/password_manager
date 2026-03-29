def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd +"\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            name, password = data.split("|")
            print(f"Name: {name} | Password: {password}")
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
