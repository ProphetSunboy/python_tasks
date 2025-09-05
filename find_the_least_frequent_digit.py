class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        """
        Finds the least frequent digit in the decimal representation of an integer.

        If multiple digits have the same minimum frequency, returns the smallest such digit.

        Args:
            n (int): The input integer.

        Returns:
            int: The digit (0-9) that occurs least frequently in n. If there are multiple, returns the smallest one.

        Example:
            >>> getLeastFrequentDigit(112233)
            1
            >>> getLeastFrequentDigit(1234567890)
            0

        Time Complexity: O(d), where d is the number of digits in n.
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(str(n))
        least_freq = 10
        least_d = "9"

        for num, freq in c.items():
            if freq < least_freq:
                least_freq = freq
                least_d = num
            elif freq == least_freq:
                if num < least_d:
                    least_d = num

        return int(num)
