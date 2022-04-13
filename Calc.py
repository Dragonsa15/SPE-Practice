from argparse import ArgumentError
import os
import math
import colorama
from colorama import Fore
from sys import platform
import os,signal

clear_cmd = ""
if platform == "linux" or platform == "linux2":
    clear_cmd = "clear"
elif platform == "win32":
    clear_cmd = "cls"

# print(clear_cmd)

class Calculator:
    def __init__(self):
        self.name = "Scintific Calculator"
    
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

    def ChoiceMapping(self,choice,params):
        output = None
        if(choice == 1):
            if(len(params) < 1):
                raise ValueError("Insufficient Params Supplied")
                
            else:
                print(Fore.GREEN +"\n\nThe square root of " + str(params[0]) + " is " + str(self.sqrt(params[0])))
                output = self.sqrt(params[0])
        if(choice == 2):
            if(len(params) < 1):
                raise ValueError("Insufficient Params Supplied")
            else:
                print(Fore.GREEN +"\n\nThe factorial of " + str(params[0]) + " is " + str(self.factorial(params[0])))
                output = self.factorial(params[0])
        if(choice == 3):
            if(len(params) < 1):
                raise ValueError("Insufficient Params Supplied")
            else:
                print(Fore.GREEN + "\n\nThe natural logarithm of " + str(params[0]) + " is " + str(self.log(params[0])))
                output = self.log(params[0])
        if(choice == 4):
            if(len(params) < 2):
                raise ValueError("Insufficient Params Supplied")
            else:
                print(Fore.GREEN +"\n\nThe power of " + str(params[0]) + " to the power of " + str(params[1]) + " is " + str(self.pow(params[0],params[1])))
                output = self.pow(params[0],params[1])
        if(choice == 5):
            os._exit(0)

        print(Fore.RED + "\n\n\nPress Enter To Continue...\n\n\n")
        input()
        return output

    def take_input(self,params):
        try:
            # Convert it into integer
            for i in range(len(params)):
                params[i] = int(params[i])
            
            return params

        except ValueError:
            raise ValueError("Insufficient Params Supplied with unknown type of values")
        
    
    def TakeNumericalInput(self,choice):
        if(choice == 1 or choice == 2 or choice == 3):
            x = input("Enter a Number : ")
            params = self.take_input([x])
            return params

        if(choice == 4):
            x = input("Enter a Number : ")
            a = input("Enter the Power : ")
            params = self.take_input([x,a])
            return params

    def step(self):
        print(Fore.WHITE)
        self.BaseScreen()
        choice = int(input("Enter your choice: "))
        params = self.TakeNumericalInput(choice)
        # print(choice)
        self.ChoiceMapping(choice,params)
        os.system(clear_cmd)

    def loop(self):
        while True:
            self.step()