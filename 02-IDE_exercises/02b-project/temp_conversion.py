#Author: Luis Mercado
#Date: 09/24/2024
#Description: Take temperature input from user (in degrees Celsius) and
#             return the temperature converted to degrees (Fahrenheit)

#Prompt to user
print("Please enter the temperature in Celsius.")

#Define variable for user input (temp in C)
temp_C: float = float(input("Temperature in Celsius"))

#Define variable for the output (temp converted to F)
temp_F: float = float((9/5)*temp_C+32)

#Display temperature converted from C to F
print("The corresponding temperature in Fahrenheit is:")
print(temp_F)

