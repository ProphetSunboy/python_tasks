class Solution:
    def get_k_based_number(self, num: int, k: int) -> list[int]:
        """Converts a given integer to its base-k representation as a list of digits (least significant digit first).

        Args:
            num (int): The integer to convert.
            k (int): The base to convert to.

        Returns:
            list[int]: The digits of num in base-k, in reverse order (least significant digit first).

        Example:
            >>> get_k_based_number(9, 2)
            [1, 0, 0, 1]  # 9 in base-2 is 1001

        Note:
            The returned list is in reverse order (least significant digit first).
        """
        reversed_based_k = []

        while num >= k:
            reversed_based_k.append(num % k)
            num //= k

        reversed_based_k.append(num)

        return reversed_based_k

    def ordered_palindrome_generator(self):
        """
        Generates palindromic numbers in increasing order.

        This generator yields all positive integers that are palindromes in base-10,
        starting from the smallest (1) and proceeding in order. It constructs palindromes
        by mirroring the digits of a "half" number, ensuring that all palindromes of a given
        length are produced before moving to longer palindromes.

        Yields:
            int: The next palindromic number in increasing order.

        Example:
            >>> gen = ordered_palindrome_generator()
            >>> [next(gen) for _ in range(10)]
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

        Note:
            - Palindromes are generated in base-10.
            - The generator produces both odd- and even-length palindromes.
        """
        length = 1
        while True:
            half_start = 10 ** ((length - 1) // 2)
            half_end = 10 ** ((length + 1) // 2)

            for half in range(half_start, half_end):
                s = str(half)
                if length % 2 == 0:
                    yield int(s + s[::-1])
                else:
                    yield int(s + s[-2::-1])

            length += 1

    def kMirror(self, k: int, n: int) -> int:
        """
        Returns the sum of the n smallest k-mirror numbers.

        A k-mirror number is a positive integer (without leading zeros) that is a palindrome in both base-10 and base-k representations.

        For example:
            - 9 is a 2-mirror number: 9 (base-10) and 1001 (base-2) are both palindromes.
            - 4 is not a 2-mirror number: 4 (base-10) is a palindrome, but 100 (base-2) is not.

        Args:
            k (int): The base in which to check for palindromicity.
            n (int): The number of k-mirror numbers to sum.

        Returns:
            int: The sum of the n smallest k-mirror numbers.

        Example:
            >>> kMirror(2, 5)
            25
            >>> kMirror(3, 7)
            499

        Time complexity: Depends on the number of palindromes generated and checked.
        Space complexity: O(1), not counting generator state.
        """
        s = 0
        palindrome_gen = self.ordered_palindrome_generator()

        while n > 0:
            num = next(palindrome_gen)
            based_k = self.get_k_based_number(num, k)

            if based_k == based_k[::-1]:
                s += num
                n -= 1

        return s
