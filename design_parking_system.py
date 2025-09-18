class ParkingSystem:
    """
    ParkingSystem is a class that simulates a parking lot with three types of parking spaces: big, medium, and small.

    Attributes:
        - big (int): Number of big parking spaces.
        - medium (int): Number of medium parking spaces.
        - small (int): Number of small parking spaces.

    Methods:
        __init__(big: int, medium: int, small: int):
            Initializes the ParkingSystem with the given number of slots for each parking space type.

        addCar(carType: int) -> bool:
            Attempts to park a car of the specified type.
            carType:
                1 - big
                2 - medium
                3 - small
            Returns True if a parking space is available for the car type and the car is parked; otherwise, returns False.

    Usage Example:
        >>> parkingSystem = ParkingSystem(1, 1, 0)
        >>> parkingSystem.addCar(1)
        True
        >>> parkingSystem.addCar(2)
        True
        >>> parkingSystem.addCar(3)
        False

    Time Complexity:
        - __init__: O(1)
        - addCar: O(1)

    LeetCode: Beats 100% of submissions
    """

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking[carType - 1] > 0:
            self.parking[carType - 1] -= 1
            return True
        else:
            return False
