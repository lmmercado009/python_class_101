#Author: Luis Mercado
#Date: 09/26/2024
#Description: Prompts user to decide a quantity of desirec number entries
#             then prompts user to enter that many numbers. Prints the min
#             and max values from the set of numbers entered.

#Define variable and prompt user for desired quantity of numbers
user_qty: int = int(input("How many numbers would you like to enter?"))

while user_qty < 1:
    print("Please enter at least 1 number.")
    user_qty: int = int(input("How many numbers would you like to enter?"))
#entire 'else' statement implies that condition is user entered >= 1 argument
else:
    print("Please enter", user_qty, "numbers:")
    
    #separate the first user entry as a starting value to compare all other inputs to
    #this makes sense here because the else statement only initiates when user enters
    #ONE OR MORE argument(s)
    first_num: int = int(input())
    
    #first user entry serves as both the min AND max until other values are added
    min_val: int = first_num
    max_val: int = first_num

    #if user enters > 1 number, run through comparisons

    while user_qty > 1:
        #define new variable for all subsequent user entries
        user_num: int = int(input())
        #iteratively compare each new entry against the existing min and max
        #if the entry meets the condition, assign it as the new min or max value
        if user_num < min_val:
            min_val = user_num
        if user_num > max_val:
            max_val = user_num
        
        #countdown statement: each loop iteration reduces the user_qty by 1
        #this ensures that after the entered number of loops are completed user_qty <1
        user_qty -= 1

    #display final results
    print("min: ", str(min_val))
    print("max: ", str(max_val))