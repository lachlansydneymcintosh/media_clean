# photo clean
first_image = input("Enter first image:        ")
last_image = input("Enter last image:         ")
file_path = input("Enter image file path:    ")

while True:
    action = input("\nProcess Selection \n[r] Rename [d] Delete\nEnter letter for process: ")

    confirmation = True
    while confirmation == True:
        if action != "r" and "d":
            print(f"Invalid selection '{action}'")
        elif action == "r":
            print("ph")
            term = "Rename"
        elif action == "d":
            print("ph")
            term = "Delete"