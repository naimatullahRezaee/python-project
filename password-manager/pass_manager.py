
pwd = input("What is the master password? ")


def view():
    pass 

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(f"{name} | {password} \n")


while True:
    mode = input("Would you like to add a new password to or veiw existing one (veiw, add) or enter q for quit? ").lower()

    if mode == "q" or mode == "quit":
        break
    if mode == "view":
        pass 
    elif mode == "add":
        add()
    else:
        print("Invalid password")
    