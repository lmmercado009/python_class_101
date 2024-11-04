#Author: Luis Mercado
#Date: 09/30/2024
#Description: Backend integer is entered that user must try to guess.
#             User is prompted to guess number. Program returns whether number
#             is higher or lower than target. If target is hit, user is told how
#             many guesses were required to hit target.

#Prompt for backend number to be guessed
print("Enter the number for the player to guess.")
target_num: int = int(input())

#Prompt user to enter their guess
print("Enter your guess.")
user_guess: int = int(input())

#Begin guess count at 1 so that if while condition is immediately met, count does not go up
guess_count: int = 1

#Set up special condition for a correct guess on first try
if user_guess == target_num:
    print("You guessed it in ", guess_count, " try.")
#For any incorrect first guesses, begin checking difference to target and give feedback to user
else:
    #Continue running loop as long as incorrect guesses are made
    while user_guess != target_num:
        #For high guess, give that feedback, reprompt user for input, and increase guess count by 1
        if user_guess > target_num:
            print("Too high - try again:")
            user_guess: int = int(input())
            guess_count += 1
        #For low guess, give that feedback, reprompt user for input, and increase guess count by 1
        elif user_guess < target_num:
            print("Too low - try again:")
            user_guess: int = int(input())
            guess_count += 1
    #Once loop is terminated by correct guess, provide the number of guesses it took to hit target
    print("You guessed it in ", guess_count, " tries.")
