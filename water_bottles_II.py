class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """
        Calculates the maximum number of water bottles you can drink given an
        initial number of full bottles and an exchange rule.

        You start with `numBottles` full water bottles. Each time you drink a bottle, it becomes an empty bottle.
        You can exchange `numExchange` empty bottles for one full bottle, but after each exchange,
        the required number of empty bottles for the next exchange increases by one.
        You cannot perform multiple exchanges at the same exchange rate in a single operation.

        Args:
            numBottles (int): The initial number of full water bottles.
            numExchange (int): The number of empty bottles required for the first exchange.

        Returns:
            int: The maximum number of water bottles you can drink.

        Example:
            >>> maxBottlesDrunk(3, 1)
            5
            >>> maxBottlesDrunk(10, 2)
            13

        Time Complexity: O(total exchanges), where each exchange increases the required empty bottles by 1.
        Space Complexity: O(1)

        LeetCode: Beats 98.89% of submissions
        """
        drinked = 0
        empty = 0

        while numBottles:
            drinked += numBottles
            empty += numBottles
            numBottles = 0

            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1

        return drinked
