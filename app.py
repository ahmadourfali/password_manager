def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("paswords.txt", "a") as f:
        f.write(name + "|" + pwd +"\n")

def view():
    pass

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
