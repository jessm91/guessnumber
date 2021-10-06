from random import randint
from random import choice

"""Generate random number between 1 and 10"""
numb = randint(1, 10)

while True:
    """Ask user to guess a number"""
    guess = input("Guess a number between 1 and 10 [enter 'q' to quit]: ")
    guess = int(guess)
    if numb == guess:
        print("You have guessed the correct number!")
        break
    else:
        print("Wrong! Guess again")
        continue
