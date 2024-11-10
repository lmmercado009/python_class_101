# Author: Luis Mercado
# Date: 11/09/2024
# Description: Function that takes two strings as arguments and returns a set
#              that contains only the words appearing in BOTH argument strings.
#              (Assumes all characters in arguments are either letters or spaces)


def words_in_both(string1: str, string2: str) -> set[str]:
    """
    Argument strings must contain only alphabetic letters and spaces
    Function returns a set containing only the words (all lower-case)
    appearing in BOTH sets, regardless of case in each string (e.g. "to" and "To" count as same word)
    """

    # convert argument strings to lists of the words in each string (all lower-case)
    list1: list[str] = string1.lower().split()
    list2: list[str] = string2.lower().split()

    # use set comprehension to create set containing only words from list1 also in list2
    word: str
    return {word for word in list1 if word in list2}

# test code
s1: str = "She's a jack of all trades"
s2: str = "Jack was tallest of all"

common_words: set[str] = words_in_both(s1, s2)
print(common_words)