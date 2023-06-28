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
            empty_bottles = empty_bottles - num_exchange * exchanged_bottles + exchanged_bottles

        return drink