#Author: Luis Mercado
#Date: 10/04/2024
#Description: Function that takes a positive integer argument, "n" and returns the
#             number at the nth position of the Fibonacci sequence

def fibonacci(position: int) -> int:
    """
    Takes an integer, n, and returns the value in the Fibonacci sequence at the nth position
    """
    #define 0th, 1st, and 2nd position terms of sequence (these will change value inside the FOR Loop of the fn.)
    fib_num_prev = 0
    fib_num_curr = 1
    fib_num_next = 1
    #Iterate through variable reassignment from 0 position to user-entry MINUS 1
    for i in range(position - 1):
        fib_num_next = fib_num_prev + fib_num_curr
        fib_num_prev = fib_num_curr
        fib_num_curr = fib_num_next
    return fib_num_next

#Test code
#test = fibonacci(2)
#print(test)

    
    
##1st attempt at solution -- it WORKED, but was not as clean as it could be with the special cases at top    
    
    #Set first 2 numbers in sequence as 1 -- not actually necessary if "for" range is defined as negative relative to position
    # INSTEAD of positive relative to position

    #fib_num_1: int = 1
    #fib_num_2: int = 1
    
    #Set special case return values for first 2 numbers in Fib sequence -- not needed with changes explained above
    #if position == 1:
    #    return fib_num_1
    #elif position == 2:
    #    return fib_num_2
    #else:
    #Run through Fib sequence to nth number (based on func argument)
    #Define next number as sum of 2 previous numbers
    #Then re-define previous 2 numbers so they move up 1 position each in sequence
    #    for n in range(3, position+1):
    #        fib_num_next: int = fib_num_1 + fib_num_2
    #        fib_num_1 = fib_num_2
    #        fib_num_2 = fib_num_next
    #return fib_num_next

#Test code
#term = fibonacci(17)
#print(term)