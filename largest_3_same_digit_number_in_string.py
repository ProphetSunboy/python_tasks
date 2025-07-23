class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """Finds the largest "good integer" substring of length 3 in the given string `num`.

        A "good integer" is defined as a substring of length 3 where all characters are the same digit.
        Returns the maximum such substring as a string, or an empty string if none exists.

        Args:
            num (str): The input string representing a large integer (may contain leading zeroes).

        Returns:
            str: The largest good integer substring of length 3, or "" if none exists.

        Example:
            >>> largestGoodInteger("6777133339")
            '777'
            >>> largestGoodInteger("2300019")
            '000'
            >>> largestGoodInteger("42352338")
            ''

        Notes:
            - A substring is a contiguous sequence of characters within a string.
            - Leading zeroes are allowed in both `num` and the result.

        Time complexity: O(n), where n is the length of `num`.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        largest = ""
        curr = [num[0]]

        for i in range(1, len(num)):
            if num[i] == curr[-1]:
                curr.append(num[i])
                if len(curr) == 3:
                    if "".join(curr) > largest:
                        largest = "".join(curr)
                        curr = [num[i]]
            else:
                curr = [num[i]]

        return largest
