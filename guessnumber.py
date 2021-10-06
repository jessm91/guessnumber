from random import randint
from random import choice

"""Generate random number between 1 and 100"""
numb = randint(1, 100)

"""Ask user to guess a number"""
guess = input("Guess a number between 1 and 100: ")

if numb == guess:
    print("You have guessed the correct number!")
else:
    print("Wrong!")
