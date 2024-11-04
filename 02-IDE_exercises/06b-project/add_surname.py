#Author: Luis Mercado
#Date: 10/18/2024
#Description: Function that takes a list of first names as a parameter, pulls out
#             only those that start with "K" and adds surname "Hoffman" to each one


def add_surname(first_names: list[str]) -> str:
    """
    Function looks for first names starting with "K" in list argument
    and returns a string of ONLY those first names with surname "Hoffman" added
    """
    
    #List comprehension that transforms each iterable of the list starting with "K"
    return [name + " Hoffman" for name in first_names if name[0] == "K"]


#Test Code
name_list: list[str] = ["Luis", "Hannah", "Kannah", "Kyla", "Fin", "Mandy"]
print(add_surname(name_list))