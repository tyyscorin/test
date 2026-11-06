"""
File: NumberGuessingGame.py
Author: Tyiis Tibbs
Created: 11/06/26
Instructor: Burgess
"""
attempts = 0


import random

secret_number = random.randint(1, 100)
print(secret_number)
while True:
    attempts = attempts + 1
    user_guess = int(input("Guess a number between 1 and 100: "))


    if user_guess == secret_number:
        break

    elif user_guess > secret_number:
        print("Too High! Try again!")

    elif user_guess < secret_number:
        print("Too Low! Try again!")


print("Congratulations! You guessed the number!")
print(f"Your total attempts: {attempts}")