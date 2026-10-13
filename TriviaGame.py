'''
Filename: Trivia Game
Author: Tyiis,Tibbs
Date: 10/05/2026
Instructor: Burgess
'''
score = 0
correct = 0
print("Welcome to Trivia Game. In a moment this program will then check the user’s inputs, and will give them a score based on how many questions they answered correctly.")
print("Please answer all following questions in lowercase.")

x =input("Multiple-choice questions are easier to grade automatically than short-answer questions? ")
if x == "false":
    print("CORRECT!")
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

g =input("What is the name of the third planet from the sun? ")
if g == "earth":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

p =input("What is the capital of france? ")
if p == "paris":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

s =input("How many continents are on earth? ")
if s == "7":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

u =input("What is the largest mammal in the world? ")
if u == "blue whale":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

v =input("What element has the chemical symbol 'O'? ")
if v == "oxygen":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

n =input("In what year did the titanic sink? ")
if n == "1912":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

m =input("How many legs does a spider have? ")
if m == "8":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

o =input("What is the hardest natural substance on Earth? ")
if o == "diamond":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

t =input("Who painted the Mona Lisa? ")
if t == "leonardo da vinci":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

e =input(" What is the main gas that makes up the Earth's atmosphere? ")
if e == "nitrogen":
    print("CORRECT!")
    correct = correct + 1
    correct = correct + 1
    score = score + 2
else:
    print("INCORRECT!")
    if score > 0:
        score = score - 2

print("score = 8/10 questions answered correctly")







































