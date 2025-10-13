class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        """
        Given a positive integer n, express n as a sum of base-10 components using
        the fewest number of components possible.

        A base-10 component is any positive integer that is the product of a single
        digit (1-9) and a non-negative power of 10.
        For example, 500, 30, and 7 are base-10 components, whereas 537, 102, and 11 are not.

        Returns:
            List[int]: A list of base-10 components that sum to n, sorted in descending order.

        Example:
            >>> decimalRepresentation(705904)
            [700000, 5000, 900, 4]
            >>> decimalRepresentation(4020)
            [4000, 20]

        Time Complexity: O(log n), where n is the input integer (proportional to the number of digits).
        Space Complexity: O(log n) for the output list.

        LeetCode: Beats 100% of submissions
        """
        ans = []

        i = 0
        while n > 0:
            curr = n % 10

            if curr > 0:
                ans.append(curr * 10**i)

            n //= 10
            i += 1

        return ans[::-1]
