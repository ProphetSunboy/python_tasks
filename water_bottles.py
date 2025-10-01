# First solution
class Solution:
    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        """
        There are numBottles water bottles that are initially full of water.
        You can exchange numExchange empty water bottles from the market with
        one full water bottle.

        The operation of drinking a full water bottle turns it into an empty
        bottle.

        Given the two integers numBottles and numExchange, return the maximum
        number of water bottles you can drink.
        """
        drink = num_bottles
        empty_bottles = num_bottles

        while empty_bottles // num_exchange > 0:
            exchanged_bottles = empty_bottles // num_exchange
            drink += exchanged_bottles
            empty_bottles = (
                empty_bottles - num_exchange * exchanged_bottles + exchanged_bottles
            )

        return drink


# Second solution
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Calculates the maximum number of water bottles you can drink given an initial
        number of full bottles and an exchange rate for empty bottles.

        You start with `numBottles` full water bottles. Each time you drink a bottle,
        it becomes empty. You can exchange `numExchange` empty bottles for one full
        bottle as many times as possible.

        Args:
            numBottles (int): The initial number of full water bottles.
            numExchange (int): The number of empty bottles required to exchange for one full bottle.

        Returns:
            int: The maximum number of water bottles you can drink.

        Example:
            >>> numWaterBottles(9, 3)
            13
            >>> numWaterBottles(15, 4)
            19

        Time Complexity: O(log(numBottles)), since the number of exchanges decreases geometrically.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        drink = 0
        empty = 0

        while numBottles > 0 or empty >= numExchange:
            numBottles += empty // numExchange
            empty %= numExchange

            drink += numBottles
            empty += numBottles
            numBottles = 0

        return drink
