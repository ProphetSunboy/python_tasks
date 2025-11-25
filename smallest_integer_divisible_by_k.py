class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Finds the length of the smallest positive integer n consisting only of the digit 1
        that is divisible by the given integer k.

        This function returns the length of the smallest n such that n % k == 0.
        If such n does not exist, returns -1.

        Args:
            k (int): The divisor.

        Returns:
            int: The length of the smallest n divisible by k, or -1 if none exists.

        Example:
            Input: k = 3
            Output: 3
            (111 is the smallest n divisible by 3.)

        Time Complexity: O(k).
        Space Complexity: O(1).
        """
        if k % 2 == 0:
            return -1

        n = 1
        digits = 1
        while digits <= k:
            if n % k == 0:
                return digits

            n = (n % k) * 10 + 1
            digits += 1

        return -1
