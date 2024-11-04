#Author: Luis Mercado
#Date: 10/22/2024
#Description: Function that takes a list of numbers and mutates it to be
#             a list of the squares of each original value - no return value


def square_list(num_list: list[float | int]) -> None:
    """
    Takes list of numbers (float or int) and mutates the list into
    a list containing the squared value of each element in original
    """
    for num in range(0,len(num_list)-1):
        num_list[num] = num_list[num]*num_list[num]


#Test code
test_list: list[float | int] = [2, 3.4, 7, 8.2]
square_list(test_list)
print(test_list)
#Cleanup notes
# instead of setting each list element equal to itself times itself,
# use **= operator to square the value