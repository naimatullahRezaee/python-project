import random 

user_win = 0
computer_win = 0

options = ['rock','paper','scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q for quit: ").lower()

    if user_input == "q" or user_input == "quit":
        break

    if user_input not in options:
        continue
    random_number = random.randint(0.2)
    # rock: 0 , paper: 1 ,scissors: 2

  