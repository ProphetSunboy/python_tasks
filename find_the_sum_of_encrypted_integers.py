class Solution:
    def encrypt(self, num: int) -> int:
        """Encrypts a given positive integer by replacing every digit with the largest digit in the number.

        The encryption function works as follows:
            - Convert the integer to a string.
            - Find the largest digit in the string.
            - Replace every digit with this largest digit.
            - Return the resulting integer.

        For example:
            encrypt(523) -> 555
            encrypt(213) -> 333

        Args:
            num (int): The positive integer to encrypt.

        Returns:
            int: The encrypted integer.
        """
        s_num = str(num)
        max_n = max(s_num)

        return int(max_n * len(s_num))

    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        """Given an integer list nums containing positive integers, returns the sum of their encrypted values.

        The encryption function encrypt(x) replaces every digit in x with the largest digit in x.
        For example, encrypt(523) = 555 and encrypt(213) = 333.

        Args:
            nums (list[int]): List of positive integers to encrypt and sum.

        Returns:
            int: The sum of the encrypted integers.

        Example:
            >>> sumOfEncryptedInt([523, 213])
            888

        Time complexity: O(n * d), where n is the number of integers and d is the average number of digits per integer.
        Space complexity: O(1)

        LeetCode: Beats 97.51% of submissions
        """
        s = 0

        for num in nums:
            s += self.encrypt(num)

        return s
