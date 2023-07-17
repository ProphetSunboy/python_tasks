class Solution:
    def guess(self, num: int) -> int:
            mystery_num = 1

            if mystery_num > num:
                return 1
            elif mystery_num < num:
                return -1
            else:
                return 0

    def guessNumber(self, n: int) -> int:
        """
        We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked.

        Every time you guess wrong, I will tell you whether the number I picked
        is higher or lower than your guess.

        You call a pre-defined function int guess(int num), which returns three
        possible results:

            -1: Your guess is higher than the number I picked (i.e. num > pick).
            1: Your guess is lower than the number I picked (i.e. num < pick).
            0: your guess is equal to the number I picked (i.e. num == pick).

        Return the number that I picked.

        LeetCode: Beats 98.21%
        """
        left, right = 0, n

        while True:
            mid = (left + right) // 2
            g = self.guess(mid)
            
            if g == -1:
                right = mid - 1
            elif g == 1:
                left = mid + 1
            else:
                return mid