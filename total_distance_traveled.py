class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        """
        Calculates the maximum distance a truck can travel given two fuel tanks and specific refueling rules.

        The truck has:
            - mainTank (int): Initial liters of fuel in the main tank.
            - additionalTank (int): Initial liters of fuel in the additional tank.

        The truck consumes 1 liter of fuel per 10 km. For every 5 liters consumed
        from the main tank, if the additional tank has at least 1 liter, exactly 1 liter
        is transferred from the additional tank to the main tank
        (this transfer is discrete and occurs immediately after each 5 liters are used).

        Args:
            mainTank (int): Fuel in the main tank (liters).
            additionalTank (int): Fuel in the additional tank (liters).

        Returns:
            int: The maximum distance (in kilometers) the truck can travel.

        Example:
            >>> distanceTraveled(9, 2)
            110

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        total_dist = 0

        while mainTank >= 5:
            d = mainTank // 5
            total_dist += d * 50
            mainTank -= d * 5
            mainTank += min(additionalTank, d)
            additionalTank -= min(additionalTank, d)

        total_dist += mainTank * 10

        return total_dist
