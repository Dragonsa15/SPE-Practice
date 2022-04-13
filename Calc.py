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

def sqrt(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def log(x):
    return math.log(x)

def pow(x,a):
    return math.pow(x,a)


def BaseScreen():
    print("Welcome to the Scientific Calculator")
    print("What do you want to do ?")
    print("● Square root function - √x")
    print("● Factorial function - x!")
    print("● Natural logarithm (base е) - ln(x)")
    print("● Power function - x")
    print("● Exit")

while True:
    print(Fore.WHITE)
    BaseScreen()
    choice = int(input("Enter your choice: "))
    print(choice)
    if(choice == 1):
        print("Enter a number: ")
        x = int(input())
        
        print(Fore.GREEN +"\n\nThe square root of " + str(x) + " is " + str(sqrt(x)))
        print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
        input()
    if(choice == 2):
        print("Enter a number: ")
        x = int(input())
        print(Fore.GREEN +"\n\nThe factorial of " + str(x) + " is " + str(factorial(x)))
        print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
        input()
    if(choice == 3):
        print("Enter a number: ")
        x = int(input())
        print(Fore.GREEN + "\n\nThe natural logarithm of " + str(x) + " is " + str(log(x)))
        print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
        input()
    if(choice == 4):
        print("Enter a number: ")
        x = int(input())
        print("Enter the power: ")
        a = int(input())
        print(Fore.GREEN +"\n\nThe power of " + str(x) + " to the power of " + str(a) + " is " + str(pow(x,a)))
        print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
        input()
    if(choice == 5):
        break

    os.system(clear_cmd)

    