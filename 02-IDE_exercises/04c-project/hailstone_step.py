#Author: Luis Mercado
#Date: 10/02/2024
#Description: Function that takes a positive integer and produces a hailstone
#             sequence that uses that input as a starting point


def hailstone_step(seq_num: int) -> int:
    """
    Function takes a positive integer as input and initiates a hailstone sequence
    starting with that positive integer.
    Once a value of "1" is achieved, the function terminates and returns the number of steps
    taken to achieve that value.
    """
    
    #Define variable for starting number of steps (0)
    step_count: int = 0
    #Include special case for negative integer being entered -- return feedback to user about input requirement
    if seq_num < 1:
        return "This function only takes positive integers as inputs"
    #For acceptable inputs, keep running hailstone steps as long as sequence number is NOT equal to 1
    #For an input of 1, the while loop never runs, so the starting step count of 0 is returned (no elif required)
    else:
        while seq_num != 1:
            if seq_num % 2 == 0:
                seq_num /= 2
                step_count += 1
            else:
                seq_num *= 3
                seq_num +=1
                step_count += 1
    return(step_count)

#Test Code
test = hailstone_step(36)
print(test)