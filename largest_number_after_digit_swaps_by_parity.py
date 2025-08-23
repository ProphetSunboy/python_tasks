class Solution:
    def largestInteger(self, num: int) -> int:
        """
        Given a positive integer num, you may swap any two digits of num that have the same parity (i.e., both odd or both even digits).

        Returns the largest possible value of num after any number of such swaps.

        Args:
            num (int): The input positive integer.

        Returns:
            int: The largest possible integer obtainable by swapping digits of the same parity.

        Example:
            >>> largestInteger(1234)
            3412
            >>> largestInteger(65875)
            87655

        Time Complexity: O(n log n), where n is the number of digits in num.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        digits = list(map(int, str(num)))

        odd = []
        even = []

        for digit in digits:
            if digit % 2:
                odd.append(digit)
            else:
                even.append(digit)

        odd.sort()
        even.sort()
        largest = []

        for d in digits:
            if d % 2:
                largest.append(str(odd.pop()))
            else:
                largest.append(str(even.pop()))

        return int("".join(largest))
