# Author: Luis Mercado
# Date: 11/06/2024
# Description: Function that takes a string argument and returns a dictionary that
#              counts how many of each letter is in that string


def count_letters(arg_string: str) -> dict[str, int]:
    """
    Takes a string as argument and returns a dictionary whose keys are each alphabet letter
    present in the string and whose values are the count of each letter.
    """

    # Create empty dictionary to which keys and values will be iteratively added
    letter_count: dict[str, int] = {}

    # Iterate through characters (all made upper-case) of arg_string, checking whether is is alphabetic,
    # If alphabetic and NOT YET IN letter_count, add key and value of 1
    # If alphabetic and already in letter_count, increase value of that key by 1

    letter: str

    for letter in arg_string:
        if "A" <= letter.upper() <= "Z":
            if letter.upper() not in letter_count:
                letter_count[letter.upper()] = 1
            else:
                letter_count[letter.upper()] += 1

    return letter_count


# Test code
test_string: str = "$ % G h g ytuCBA"
print(count_letters(test_string))