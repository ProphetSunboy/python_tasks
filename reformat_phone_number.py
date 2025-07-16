class Solution:
    def reformatNumber(self, number: str) -> str:
        """Reformats a phone number string according to specific grouping rules.

        The input string may contain digits, spaces, and/or dashes. The function removes all spaces and dashes,
        then groups the digits from left to right into blocks of length 3 until 4 or fewer digits remain.
        The final digits are grouped as follows:
            - 2 digits: one block of 2
            - 3 digits: one block of 3
            - 4 digits: two blocks of 2

        The blocks are joined by dashes. No block of length 1 is ever produced, and at most two blocks of length 2.

        Args:
            number (str): The input phone number string.

        Returns:
            str: The reformatted phone number.

        Example:
            >>> reformatNumber("1-23-45 6")
            '123-456'
            >>> reformatNumber("123 4-567")
            '123-45-67'
            >>> reformatNumber("123 4-5678")
            '123-456-78'

        Time complexity: O(n), where n is the length of the input string.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        num = number.replace("-", " ")
        num = "".join(num.split())

        formatted = ""
        i = 0
        j = len(num)

        while j > 4 and i < len(num):
            formatted += num[i : i + 3] + "-"
            i += 3
            j -= 3

        if j == 2:
            formatted += num[len(num) - 2 :]
        elif j == 3:
            formatted += num[len(num) - 3 :]
        elif j == 4:
            formatted += num[len(num) - 4 : len(num) - 2] + "-" + num[len(num) - 2 :]

        return formatted.rstrip("-")
