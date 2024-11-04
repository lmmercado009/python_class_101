#Author: Luis Mercado
#Date: 10/06/2024
#Description: A recursive function that takes two positive integers as arguments
#             and returns the product of those two numbers WITHOUT using multiplicaiton or loops


def multiply(num_1: int, num_2: int) -> int:
    """
    Function that produces the product of two arguments by
    using ONLY addition (no multiplication OR loops)
    """

    if num_1 == 0: #define first of 4 base cases when either input is 0 or 1
        return print("Arguments must be positive integers.")
    elif num_2 == 0:
        return print("Arguments must be positive integers.")
    elif num_1 == 1:
        return num_2
    return multiply(num_1 - 1, num_2) + num_2

print(multiply(267,2))