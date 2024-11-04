#Author: Luis Mercado
#Date: 10/01/2024
#Description: Function that takes a positive integer argument, "n" and returns the
#             number at the nth position of the Fibonacci sequence

def fibonacci(position: int) -> int:
    """
    Takes an integer, n, and returns the value in the Fibonacci sequence at the nth position
    """

    #Set first 2 numbers in sequence as 1
    fib_num_1: int = 1
    fib_num_2: int = 1
    
    #Set special case return values for first 2 numbers in Fib sequence
    if position == 1:
        return fib_num_1
    elif position == 2:
        return fib_num_2
    else:
    #Run through Fib sequence to nth number (based on func argument)
    #Define next number as sum of 2 previous numbers
    #Then re-define previous 2 numbers so they move up 1 position each in sequence
        for n in range(3, position+1):
            fib_num_next: int = fib_num_1 + fib_num_2
            fib_num_1 = fib_num_2
            fib_num_2 = fib_num_next
    return fib_num_next

#Test code
#term = fibonacci(17)
#print(term)