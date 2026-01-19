class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Given a string n representing a positive decimal integer, return the minimum number
        of positive deci-binary numbers needed so that they sum up to n.

        A decimal number is called deci-binary if each of its digits is either 0 or 1
        without any leading zeros. For example, 101 and 1100 are deci-binary, while
        112 and 3001 are not.

        Args:
            n (str): Input string representing a positive decimal integer.

        Returns:
            int: The minimum number of positive deci-binary numbers required to sum to n.

        Example:
            Input:
                n = "32"
            Output:
                3

        Time Complexity: O(len(n)), where len(n) is the length of the string n.
        Space Complexity: O(1)

        LeetCode: Beats 93.14% of submissions
        """
        return int(max(set(n)))
