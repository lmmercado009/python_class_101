#Author: Luis Mercado
#Date: 10/24/2024
#Description: Function that mutates a list of numbers by reversing its order without slicing


def reverse_list(num_list: list[int | float]) -> None:
    """
    Mutates list of numbers (float or int) into reverse order
    without using any slicing (no return value)
    """
    
    #define lower limit of desired index range which is actually upper limit of starting list argument
    low_lim: int = len(num_list)-1
    
    #for range must use negative stride and go to -1 so that 0 index is actually included
    for num in range(low_lim, -1, -1):
        num_list.append(num_list[num]) #adds currently indexed list value to end of list
        del num_list[num] #deletes original interation of currently indexed value from list

    #no return value, but by using .append and del[], the original num_list argument has iteratively had its last
    #value duplicated to the end and then had the original occurrence of it deleted so that the list is now
    #effectively in the opposite order

#Test code
test_list: list[float | int] = [2, -5, 10, 9]
reverse_list(test_list)
print(test_list)