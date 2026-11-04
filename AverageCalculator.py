"""
Filename: NumberGuessingGame.py
Author: Tyiis Tibbs
Created: 10/27/26
Intructor: Burgess
"""

total = 0
num = 0
again = "y"

while again == "y":
    x = int(input("Enter a number: "))

    total = total + x
    num = num + 1
    average = total / num

    print(f"sum = {total}")
    print(f"total numbers entered {num}")
    print(f"average = {average}")

    #conditional change here
    again = input("Would you like to input another number? (y/n)")


print("Goodbye thank you for using the Average Calculator!")
