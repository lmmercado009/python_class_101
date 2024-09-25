#Author: Luis Mercado
#Date: 09/24/2024
#Description: Calculates the least number of coins required to make change
#             based on an integer number of cents input by the user

#Prompt the user
print("Please enter an amount between 0 and 99 cents.")

#Define variable for user-input cent quantity
user_cents: int = int(input("For how may cents do you require change?"))

#In order to provide user with the least total number of coins, the user must
#be provided with the most possible of each coin in descending value, starting with quarters

#Define variables for the monetary value of each coin type (in cents)
q_val: int = 25
d_val: int = 10
n_val: int = 5
p_val: int = 1

#Define variable for the highest number of quarters that can be provided to the user
max_quart: int = int(user_cents // q_val)
#Re-define remaining cents after giving max quarters
user_cents -= max_quart * q_val
#Define variable for highest number of dimes that can be provided to the user
max_dime: int = int(user_cents // d_val)
#Re-define remaining cents after giving max dimes
user_cents -= max_dime * d_val
#Define variable for the highest number of nickels that can be provided to the user
max_nick: int = int(user_cents // n_val)
#Re-define remaining cents after giving max nickels
user_cents -= max_nick * n_val
#Define variable for the highest number of pennies that can be provided to the user
max_penn: int = int(user_cents // p_val)
#Re-define remaining cents after giving max pennies (keep in backend for test, should be 0)
user_cents -= max_penn * p_val

print("Your change will be:")
print("Q: " + str(max_quart))
print("D: " + str(max_dime))
print("N: " + str(max_nick))
print("P: " + str(max_penn))