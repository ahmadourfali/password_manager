def add():
    pass
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
