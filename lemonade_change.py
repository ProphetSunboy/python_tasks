class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        """
        Given an integer array bills where bills[i] is the bill the ith customer
        pays, return True if you can provide every customer with the correct
        change, or False otherwise.

        At a lemonade stand, each lemonade costs $5. Customers are standing in
        a queue to buy from you and order one at a time (in the order specified
        by bills). Each customer will only buy one lemonade and pay with either
        a $5, $10, or $20 bill. You must provide the correct change to each
        customer so that the net transaction is that the customer pays $5.

        Note that you do not have any change in hand at first.

        :param list[int] bills: list of bills
        :returns bool change_possible: the correct change for each client can be provided

        Time complexity: O(n)
        Space complexity: O(1)


        LeetCode: Beats 98.79%
        """
        change = [0] * 3

        for bill in bills:
            if bill == 5:
                change[0] += 1
            else:
                if bill == 10:
                    change[0] -= 1
                    change[1] += 1
                else:
                    if change[1] > 0:
                        change[1] -= 1
                        change[0] -= 1
                        change[2] += 1
                    else:
                        change[0] -= 3
                        change[2] += 1

                if change[0] < 0 or change[1] < 0:
                    return False

        return True
