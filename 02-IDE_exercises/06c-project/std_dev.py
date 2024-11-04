#Author: Luis Mercado
#Date: 10/18/2024
#Description: Creates a class, Person, containing 2 private instance variables (name and age)
#             Also creates a function, std_dev that takes a list of Person objects and returns
#             the standard deviation of their ages



class Person:
    """
    Represents an object-type of "person" defined by the person's name and age
    """

    def __init__(self, person_name: str, person_age: int):
        """
        Initializes the defining values of Person as the user-entered arguments
        """

        self._person_name: str = person_name
        self._person_age: int = person_age
    
    def get_age(self):
        """
        Returns the age of a Person
        """

        return self._person_age
    

def std_dev(people_list: list[Person]) -> float:
    """
    Takes a list of objects in Person class and calculates the
    standard deviation of all the ages attached to the People in the list
    """
    
    #Set a starting variable that will hold the iteratively summed ages of the list
    sum_ages: int = 0

    #Find the average of all ages by summing and dividing by the number of objects in list
    for people in people_list:
        sum_ages += people.get_age()
    
    avg_age: float = sum_ages / len(people_list)

    #Set a starting variable that will hold the iteratively summed variances
    diff_sq: int = 0

    #Find the variance values for each age in list
    for people in people_list:
        diff_sq += (people.get_age() - avg_age)**2
    
    #Find average variance
    variance: float = diff_sq / len(people_list)

    #Define standard deviation as the square root of the average variance
    std_dev = variance**0.5
    return std_dev




#Test code
person1 = Person("Luis", 30)
person2 = Person("Hannah", 28)
person3 = Person("Kyla", 8)

person_list: list[Person] = [person1, person2, person3]
answer = std_dev(person_list)
print(answer)
