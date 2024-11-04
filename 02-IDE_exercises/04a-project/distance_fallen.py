#Author: Luis Mercado
#Date: 10/01/2024
#Description: Function that takes a time quantity from user (in seconds)
#             and calculates the distance (in meters) fallen during that time

def distance_fallen(time_sec: float) -> float:
    """
    Takes a length of time in seconds and returns the distance fallen in 
    that time due to gravity based on the formula d = (1/2)*g*t^2 where
    d is distance, g is gravitational constant, and t is the entered argument
    """
    #define gravitational constant (acceleration)
    g: float = 9.8
    return (1/2) * g * time_sec ** 2

#Test script
#dist = distance_fallen(4.5)
#print(dist)