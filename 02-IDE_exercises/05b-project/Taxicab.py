#Author: Luis Mercado
#Date: 10/06/2024
#Description: Class representing a Taxicab by its x-y coordinates and miles driven (odometer)


class Taxicab:
    """
    Represents a Taxicab with a position defined by x-y coordinates and mileage driven defined by
    an odometer entry
    """

    def __init__(self, x_coord: int, y_coord: int):
        """
        Creates a Taxicab with starting position of x_coord, y_coord
        and an odometer reading of 0
        """
        self._x_coord: int = x_coord
        self._y_coord: int = y_coord
        self._odometer: int = 0

    def get_x_coord(self):
        """
        Returns the current x-position of the cab
        """
        return self._x_coord
    
    def get_y_coord(self):
        """
        Returns the current y-position of the cab
        """
        return self._y_coord
    
    def get_odometer(self):
        """
        Returns the current odometer reading on the cab based on
        distance moved
        """
        return self._odometer
    
    #Method assumes movement left is negative and movement right is positive
    def move_x(self, x_dist: int):
        """
        Takes a distance in units and instructs cab to move that many units left or right
        from current position
        """
        self._x_coord += x_dist
        self._odometer += abs(x_dist)
    
    #Method assumes movement down is negative and movement up is positive
    def move_y(self, y_dist: int):
        """
        Takes a distance in units and instructs cab to move that many units
        up or down from current position
        """
        self._y_coord += y_dist
        self._odometer += abs(y_dist)
    

#Test code
cab = Taxicab(3, -8)
print(cab.get_odometer())
print(cab.get_y_coord())
cab.move_x(-10)
cab.move_y(18)
print(cab.get_x_coord())
print(cab.get_y_coord())
print(cab.get_odometer())