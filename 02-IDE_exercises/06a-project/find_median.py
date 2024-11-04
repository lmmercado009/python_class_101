#Author: Luis Mercado
#Date: 10/16/2024
#Description: Function  that takes a list of numbers as agrument and returns
#             the median of those numbers


def find_median(number_list: list[float]) -> float:
    """
    Function takes a list of numbers (in this case floats) as argument,
    sorts them in ascending order, and finds the median of the number list.
    Result is given simply if list contains odd number of float values, but if
    list contains even count of float values, the average of the two middle-most numbers
    is returned instead, following the math logic of median calculation.
    """

    #sort the list
    number_list.sort()

    #set up variable for the length of the list, which is the same as the final index of the string + 1
    count: int = len(number_list)
    #set up variables for key indices: in odd case, mid_ind finds the middle index by halving the string length
    #and rounding down
    mid_ind: int = int(count // 2)
    #since in even case, mid_ind will refer to half the len(), it is 1 index above the middle
    alt_ind: int = int(mid_ind - 1)
    
    #sets first condition for lists with even number of values
    if count % 2 == 0:
        return (number_list[mid_ind] + number_list[alt_ind]) / 2 #finds the average of the middle 2 values
    #sets second condition for lists with odd number of values
    else:
        return number_list[mid_ind] #finds the true middle value

#Test code
odd_list: list[float] = [-2.5, 7, 1]
even_list: list[float] = [-3.4, 2, -6.8, -17, 5, 3, 27, 19]
print(find_median(even_list))
print(find_median(odd_list))