"""
 Filename: conditional_calculator.py
 Author: Tyiis Tibbs
 Created: 09/30/26
"""
print("Welcome to the Conditional Calculator! The calculator will ask the user to input their first number, then input the operation they desire to perform, and then their second number. The calculator will then perform only the operation that the user requested. ")


n1 = int(input("Enter the first number"))
op=input("Enter the operation")
n2 = int(input("Enter the second number"))
if op=="+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif op=="-":
    print(f"{n1} - {n2} = {n1 - n2}")

elif op=="*":
    print(f"{n1} * {n2} = {n1 * n2}")

elif op=="/":
    print(f"{n1} / {n2} = {n1 / n2}")
print("Thank you for using the Conditional Calculator")