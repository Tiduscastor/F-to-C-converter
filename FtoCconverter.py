# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:48:55 2024

@author: patri
"""
# Fahrenheit to Celsius converter
while True:
    try:
        # This tries to store the given input as a float, and if it isn't a number, it moves to the exception statement.
        fahrenheit = float(input("Type the Fahrenheit temperature you would like to be converted to Celsius: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} degrees Fahrenheit is about: {round(celsius)} degrees Celsius!\n")  # Rounding Celsius for readability

        user_input = input("Would you like to convert another temperature? Type Y for yes or N for no: ").upper()

        if user_input == "N":
            break
        elif user_input != "Y":
            # Giving the user another chance to follow the given directions.
            user_input = input("Enter 'Y' to continue or 'N' to stop: ").upper()
            if user_input != "Y":
                break  # If the user inputs something other than Y/y or N/n AGAIN, the code will just break.

    except ValueError:  # ValueError is raised if the 'Try' code fails to convert the input to a float.
        print("Please enter a number")
