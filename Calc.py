import os
import math
import colorama
from colorama import Fore
from sys import platform

clear_cmd = ""
if platform == "linux" or platform == "linux2":
    clear_cmd = "clear"
elif platform == "win32":
    clear_cmd = "cls"

print(clear_cmd)

class Calculator:
    def __init__(self,name):
        self.name = name

    def sqrt(self,x):
        return math.sqrt(x)

    def factorial(self,x):
        return math.factorial(x)

    def log(self,x):
        return math.log(x)

    def pow(self,x,a):
        return math.pow(x,a)


    def BaseScreen(self):
        print("Welcome to the Scientific Calculator")
        print("What do you want to do ?")
        print("● Square root function - √x")
        print("● Factorial function - x!")
        print("● Natural logarithm (base е) - ln(x)")
        print("● Power function - x")
        print("● Exit")

    def CalcStart(self):
        while True:
            print(Fore.WHITE)
            self.BaseScreen()
            choice = int(input("Enter your choice: "))
            print(choice)
            if(choice == 1):
                print("Enter a number: ")
                x = int(input())
                
                print(Fore.GREEN +"\n\nThe square root of " + str(x) + " is " + str(self.sqrt(x)))
                print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
                input()
            if(choice == 2):
                print("Enter a number: ")
                x = int(input())
                print(Fore.GREEN +"\n\nThe factorial of " + str(x) + " is " + str(self.factorial(x)))
                print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
                input()
            if(choice == 3):
                print("Enter a number: ")
                x = int(input())
                print(Fore.GREEN + "\n\nThe natural logarithm of " + str(x) + " is " + str(self.log(x)))
                print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
                input()
            if(choice == 4):
                print("Enter a number: ")
                x = int(input())
                print("Enter the power: ")
                a = int(input())
                print(Fore.GREEN +"\n\nThe power of " + str(x) + " to the power of " + str(a) + " is " + str(self.pow(x,a)))
                print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
                input()
            if(choice == 5):
                break

            os.system(clear_cmd)

