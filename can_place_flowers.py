class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        Given list flowerbed and number of flowers to be placed,
        return True if n new flowers can be planted in the flowerbed.

        You have a long flowerbed in which some of the plots are planted, and
        some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer list flowerbed containing 0's and 1's, where 0 means
        empty and 1 means not empty, and an integer n, return True if n new
        flowers can be planted in the flowerbed without violating the
        no-adjacent-flowers rule and false otherwise.

        :param list[int] flowerbed: list, containing 0's and 1's
        :param int n: number of flowers
        :returns bool res: True if n flowers can be planted in flowerbed, False otherwise

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 99.98%
        """
        if n == 0:
            return True

        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

                    if n <= 0:
                        return True

        return False
