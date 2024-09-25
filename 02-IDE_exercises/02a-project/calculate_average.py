#Author: Luis Mercado
#Date: 09/23/2024
#Description: Asks the user for 5 numbers as input (including negatives) and
#             calculates the average of those numbers (including if negative)

#Prompt to user
print("Please enter five numbers.")
#Define variables for each of the five numbers user will input
user_num_1: float = float(input("Enter your 1st number:"))
user_num_2: float = float(input("Enter your 2nd number:"))
user_num_3: float = float(input("Enter your 3rd number:"))
user_num_4: float = float(input("Enter your 4th number:"))
user_num_5: float = float(input("Enter your 5th number:"))
#Define variable for the average of the 5 user-entered numbers
user_calc_avg: float = float((user_num_1 + user_num_2 + user_num_3 + user_num_4 + user_num_5)/5)
#Print explaining phrase followed by value of calculated average on new line
print("The calculated average of those numbers is:" + str(user_calc_avg))