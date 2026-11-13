"""
Filename: factorial_calculator.py
Author: Tyiis Tibbs
Created: 11/10/2026
Instructor: Burgess
"""

def factorial():
        num = int(input("Enter a non-negative whole number on the line below.\n"))
        total = 1

        if num == 0:
            print("0! = 1")
        else:
            print(f"{num}! =", end=" ")
            for x in range(num, 0, -1):
                total = total * x
                if x > 1:
                    print(x, end=" * ")
                else:
                    print(f"{x} = {total}")


# You should not need to change any code below this point

def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()