class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Returns the k-th lexicographical happy string of length n.

        A happy string is defined as a string:
          - Consisting only of the characters 'a', 'b', and 'c'.
          - No two adjacent characters are the same (i.e., for all valid i, s[i] != s[i+1]).

        Given two integers n and k, consider the list of all happy strings of length n
        sorted lexicographically. Return the k-th string of this list (1-indexed),
        or an empty string if there are fewer than k happy strings of length n.

        Args:
            n (int): Length of the happy strings to generate.
            k (int): The 1-based index of the desired happy string.

        Returns:
            str: The k-th lexicographical happy string of length n,
            or an empty string if it does not exist.

        Example:
            Input: n = 3, k = 9
            Output: "cab"

        Time Complexity: O(3 * 2^(n-1)), since each string branches into two
        new happy strings at every step after the first character.
        Space Complexity: O(3 * 2^(n-1)), due to storage of all happy strings of length n.
        """
        happy_s = ["a", "b", "c"]

        if k > 3 * 2 ** (n - 1):
            return ""

        for _ in range(n - 1):
            curr = []
            for s in happy_s:
                if s[-1] == "a":
                    curr.append(s + "b")
                    curr.append(s + "c")
                elif s[-1] == "b":
                    curr.append(s + "a")
                    curr.append(s + "c")
                else:
                    curr.append(s + "a")
                    curr.append(s + "b")

            happy_s = curr

        return happy_s[k - 1]
