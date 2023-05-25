from math import gcd

class Solution:
    def partition_is_possible(self, arr: List[int], divisor: int) -> bool:
        """
        Divide given group sizes by divisor.
        Return True if all divisions proceeds without remainders,
        False otherwise.
        """
        for num in arr:
            if num / divisor != num // divisor:
                return False
        return True

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        Given an integer array deck where deck[i] represents the number
        written on the ith card.

        Partition the cards into one or more groups such that:

            Each group has exactly x cards where x > 1, and
            All the cards in one group have the same integer written on them.

        Return true if such partition is possible, or false otherwise.
        """
        unique_items = set(deck)
        group_sizes = [0] * len(unique_items)

        for i, num in enumerate(unique_items):
            group_sizes[i] = deck.count(num)

        if min(group_sizes) < 2:
            return False

        divisor = gcd(*group_sizes)
        if divisor == 1:
            return False

        return self.partition_is_possible(group_sizes, divisor)