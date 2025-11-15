class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Given a binary string s, returns the number of substrings with "dominant ones".

        A substring has dominant ones if the number of '1's in the substring is
        greater than or equal to the square of the number of '0's in that substring:
            ones_count >= (zeros_count) ** 2

        Args:
            s (str): The input binary string.

        Returns:
            int: The number of substrings with dominant ones.

        Example:
            Input:  s = "101"
            Output: 5

            Explanation:
                The substrings with dominant ones are: "1", "0", "1", "10", and "101".

        Time Complexity: O(n^2) in the worst case for the current approach.
        Space Complexity: O(n).
        """
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res
