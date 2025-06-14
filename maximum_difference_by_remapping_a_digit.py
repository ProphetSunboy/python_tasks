class Solution:
    def minMaxDifference(self, num: int) -> int:
        """Calculates the maximum possible difference between two numbers created by remapping digits.

        Given an integer num, finds the difference between the maximum and minimum values that can be
        created by remapping exactly one digit to another digit (0-9).

        Rules:
        - One digit can be remapped to any other digit (including itself)
        - All occurrences of the chosen digit are replaced
        - Different digits can be remapped for max and min values
        - Leading zeros are allowed in the result

        Args:
            num (int): The input number to remap digits from

        Returns:
            int: The difference between maximum and minimum possible values after remapping

        Examples:
            >>> minMaxDifference(11891)
            99009  # Max: 99899 (remap 1->9), Min: 890 (remap 1->0)
            >>> minMaxDifference(90)
            99  # Max: 99 (remap 0->9), Min: 0 (remap 9->0)

        Time complexity: O(n) - where n is number of digits in num
        Space complexity: O(n) - for string conversion
        """
        s_num = str(num)
        min_num = int(s_num.replace(s_num[0], "0"))
        idx = 0

        for i, ch in enumerate(s_num):
            if ch < "9":
                idx = i
                break

        max_num = int(s_num.replace(s_num[idx], "9"))

        return max_num - min_num
