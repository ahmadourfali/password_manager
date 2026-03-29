while True:
    mode = input("would you like to view password or create a new one?"
    "(view/add) or click quit to end the program: ").lower()
    
    if mode == "quit":
        print("See you soon!")
        break
    if mode == "view":
        print("view ")
    elif mode == "add":
        print("add")
    else:
        print("Invalid mode!")
        continue
