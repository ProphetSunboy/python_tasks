class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        """Simulates picking gifts from the richest pile for k seconds.

        At each second:
            1. Choose the pile with the maximum number of gifts.
            2. Reduce the number of gifts in that pile to the floor of its square root.

        Args:
            gifts (list[int]): List of integers representing the number of gifts in each pile.
            k (int): Number of seconds to perform the operation.

        Returns:
            int: Total number of gifts remaining after k seconds.

        Example:
            >>> pickGifts([25, 64, 9, 4, 100], 4)
            29

        Time complexity: O(k * n), where n is the number of piles.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        gifts.sort()
        while k > 0:
            if gifts[-1] == 1:
                break

            max_gift = gifts.pop()
            gift = int(max_gift**0.5)

            if not gifts or gift < gifts[0]:
                idx = 0
            elif gift > gifts[-1]:
                idx = len(gifts)
            else:
                for i in range(len(gifts) - 1):
                    if gift >= gifts[i] and gift <= gifts[i + 1]:
                        idx = i + 1
                        break

            gifts.insert(idx, gift)
            k -= 1

        return sum(gifts)
