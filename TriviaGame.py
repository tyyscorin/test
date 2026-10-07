'''
Filename: Trivia Game
Author: Tyiis,Tibbs
Date: 10/05/2026
Instructor: Burgess
'''
score = 0
correct = 0
print("Welcome to Trivia Game. In a moment this program will then check the user’s inputs, and will give them a score based on how many questions they answered correctly.")
print("Please answer all following questions lowercase.")

x =input("Multiple-choice questions are easier to grade automatically than short-answer questions? ")
if x == "false":
    print("CORRECT!")
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")




