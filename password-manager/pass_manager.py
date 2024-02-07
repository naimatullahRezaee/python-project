
pwd = input("What is the master password? ")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print(f" Username: {user}\n Password: {passw} ")

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(f"{name} | {password} \n")


while True:
    mode = input("Would you like to add a new password to or view existing one (view, add) or enter q for quit? ").lower()

    if mode == "q" or mode == "quit":
        break
    if mode == "view":
        view() 
    elif mode == "add":
        add()
    else:
        print("Invalid password")
    