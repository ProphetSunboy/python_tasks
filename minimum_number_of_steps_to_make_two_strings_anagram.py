class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Given two strings s and t of equal length, this function returns the minimum
        number of steps required to make t an anagram of s. In one step, you may
        replace any character of t with any other character.

        An anagram of a string is a string formed by rearranging the letters of the
        string to produce a new string, using all original characters exactly once.

        Args:
            s (str): The target string.
            t (str): The initial string to be transformed.

        Returns:
            int: The minimum number of character replacements needed to make t
            an anagram of s.

        Example:
            Input: s = "bab", t = "aba"
            Output: 1
            Explanation: Replace t[0] = 'a' with 'b' to make t = "bba", which is
            an anagram of "bab".

        Time Complexity: O(N), where N is the length of the strings.
        Space Complexity: O(1), limited by the size of the alphabet.

        LeetCode: Beats 94.11% of submissions
        """
        c_s = Counter(s)
        c_t = Counter(t)

        ops = 0

        for ch in c_s:
            if c_s[ch] > c_t[ch]:
                ops += c_s[ch] - c_t[ch]

        return ops
