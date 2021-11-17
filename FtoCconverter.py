# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 03:17:18 2021

@author: patrick
"""

#Fahrenheit to Celsius converter
running = True

while running == True:
    try: #This trys to store the given input as a float and if the given input isn't a number then it moves to the exception statement.
        F = float(input("Type the Fahrenheit temperature you would like to be converted to Celsius: "))
        C = ((F - 32) * 5) / 9
        print()
        print(F, "degrees Fahrenheit is about:", round(C), "degrees Celsius!\n") #The rounding of Celsius here is because no one likes decimal temps.
        x = input("Would you like to convert another temperature? Type Y for yes or N for no: ")
        
        if x.upper() == "Y":
            pass
        elif x.upper() == "N":
            break
        else: 
           y = input("Enter 'Y' to continue or 'N' to stop: ") #This line gives the user another chance to follow the given directions.
           if y.upper() == "Y":
                pass
           else: 
                break #If the user inputs something other than Y/y or N/n AGAIN then the code will just break.
        
    except ValueError: #ValueError is something I just learned you can call in case the 'Try' code fails to actualize. Nifty!
        print("Please enter a number")