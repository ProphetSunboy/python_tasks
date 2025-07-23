class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """Given a string s consisting of digits and an integer k, repeatedly perform
        the following operation until the length of s is less than or equal to k:

            1. Divide s into consecutive groups of size k (the last group may be shorter).
            2. For each group, compute the sum of its digits and convert the sum to a string.
            3. Concatenate all resulting strings to form the new s.

        Return the final string s after all rounds are completed.

        Args:
            s (str): The input string consisting of digits.
            k (int): The group size for each round.

        Returns:
            str: The resulting string after all rounds.

        Example:
            >>> digitSum("11111222223", 3)
            '135'
            # Explanation:
            # Round 1: "111", "112", "222", "23" -> sums: 3, 4, 6, 5 -> "3465"
            # Round 2: "346", "5" -> sums: 13, 5 -> "135"
            # Round 3: length <= k, so return "135"

        Time complexity: O(n log n), where n is the length of s.
        Space complexity: O(n).

        LeetCode: Beats 100% of submissions
        """
        while len(s) > k:
            nums = []

            for i in range(0, len(s), k):
                num = str(sum(map(int, s[i : i + k])))
                nums.append(num)

            s = "".join(nums)

        return s
