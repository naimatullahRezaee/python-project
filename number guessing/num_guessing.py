
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
         