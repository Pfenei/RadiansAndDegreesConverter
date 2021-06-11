# Radian/Degrees Calculator
import math

answer = "y"

while answer != "n":

    case = input("What would you like to calculate? 1 - radians to degrees / 2 - degrees to radians: ")

    if case == "1":
        radians = float(input("Enter Radian Amount: "))
        total = radians * 180 / math.pi
        print(radians, "radians are ", round(total, 2), "degrees.")
        answer = input("Would you like to do any other calculation? (y/n)").lower()
    elif case == "2":
        degrees = float(input("Enter Degrees Amount: "))
        total = degrees * math.pi / 180
        print(degrees, "degrees are ", round(total, 2), "pi radians.")
        answer = input("Would you like to do any other calculation? (y/n)").lower()
    else:
        print("Wrong option, choose again.")

print("Thanks for using the app!")