class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        """
        We have a wooden plank of the length n units. Some ants are walking on
        the plank, each ant moves with a speed of 1 unit per second. Some of the
        ants move to the left, the other move to the right.

        When two ants moving in two different directions meet at some point,
        they change their directions and continue moving again. Assume changing
        directions does not take any additional time.

        When an ant reaches one end of the plank at a time t, it falls out of
        the plank immediately.

        Given an integer n and two integer lists left and right, the positions
        of the ants moving to the left and the right, return the moment when the
        last ant(s) fall out of the plank.

        :param int n: integer
        :param list[int] left: integer list
        :param list[int] right: integer list
        :returns int t: moment when the last ant(s) fall out of the plank

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 97.84%
        """
        max_l = 0
        min_r = n + 1

        for num in left:
            if num > max_l:
                max_l = num

        for num in right:
            if num < min_r:
                min_r = num

        t = max_l

        if n - min_r > t:
            t = n - min_r

        return t
