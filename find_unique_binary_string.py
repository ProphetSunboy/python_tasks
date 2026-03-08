class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Given a list of unique binary strings `nums` containing n binary
        strings, each of length n, return a binary string of length n that does
        not appear in `nums`.
        If there are multiple answers, you may return any of them.

        Args:
            nums (List[str]): List of unique binary strings of length n.

        Returns:
            str: A binary string of length n not present in `nums`.

        Example:
            Input: nums = ["01", "10"]
            Output: "00" or "11"

        Time Complexity: O(n), where n is the length of each string and the
                count of strings.
        Space Complexity: O(1), as only a constant amount of extra space is
                used.

        LeetCode: Beats 100% of submissions
        """
        num = 0

        while bin(num)[2:].zfill(len(nums)) in nums:
            num += 1

        return bin(num)[2:].zfill(len(nums))
