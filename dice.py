#It is a very basic Dice roller game made in Python.
#Just enter 'y' if you want to roll again and again and 'n' if you're done.

import random


def diceFace(num):
    if num == 1:
        print("========")
        print("|     " + " |")
        print("|   " + "0" + "  |")
        print("|     " + " |")
        print("========")

    if num == 2:
        print("========")
        print("|     " + " |")
        print("|  " + "00" + "  |")
        print("|     " + " |")
        print("========")

    if num == 3:
        print("========")
        print("|     " + " |")
        print("|  " + "000" + " |")
        print("|     " + " |")
        print("========")

    if num == 4:
        print("========")
        print("|     " + " |")
        print("|   " + "00" + " |")
        print("|   " + "00" + " |")
        print("========")

    if num == 5:
        print("========")
        print("|  " + "0 0" + " |")
        print("|   " + "0" + "  |")
        print("|  " + "0 0" + " |")
        print("========")

    if num == 6:
        print("========")
        print("|  " + "0 0" + " |")
        print("|  " + "0 0" + " |")
        print("|  " + "0 0" + " |")
        print("========")


diceFaceNum = random.randint(1, 6)

str = 'y'
while str == 'y':
    if diceFaceNum == 1:
        diceFace(1)
    elif diceFaceNum == 2:
        diceFace(2)
    elif diceFaceNum == 3:
        diceFace(3)
    elif diceFaceNum == 4:
        diceFace(4)
    elif diceFaceNum == 5:
        diceFace(5)
    elif diceFaceNum == 6:
        diceFace(6)
    print("Would you like to roll once again ?")
    str = input("Enter y for yes and n for a no\n")
