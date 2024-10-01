#Author: Luis Mercado
#Date: 09/30/2024
#Description: takes a user-entered POSITIVE INTEGER and returns
#             all factors from 1 up to the user-entered number (inclusive)

#Prompt user and define input variable
print("Please enter a POSITIVE integer: ")
user_dividend: int = int(input())

#Ensure user actually enters a positive integer, otherwise return to prompt
while user_dividend < 1:
    print("Your entry must be a POSITIVE integer - please enter: ")
    user_dividend: int = int(input())
#Once a positive integer (>0) is entered, move to testing for factors of user entry
else:
    #Print header of output
    print("The factors of ", user_dividend, " are:")
    
    #Iterate through integers from 1 to user entry
    #If entry is divisible by integer, print it
    for num in range(1, (user_dividend + 1)):
        if user_dividend % num == 0:
            print(num)

#Loop ends once nested FOR loop has run through rull range of integers