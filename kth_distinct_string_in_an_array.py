class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        """Finds the kth distinct string in a list.

        A distinct string is a string that appears exactly once in the list.
        Strings are considered in their original order of appearance.

        Args:
            arr (list[str]): A list of strings to search through
            k (int): The position of the distinct string to find (1-based index)

        Returns:
            str: The kth distinct string, or empty string if fewer than k distinct strings exist

        Example:
            >>> kthDistinct(["d","b","c","b","c","a"], 2)
            "a"  # "d" is 1st distinct, "a" is 2nd distinct

        Time complexity: O(n) - where n is length of arr
        Space complexity: O(n) - to store character counts

        LeetCode: Beats 100% of submissions
        """
        c = Counter(arr)

        n = 1
        distinct_string = ""
        for s in arr:
            if c[s] == 1:
                if n == k:
                    distinct_string = s
                    break
                else:
                    n += 1

        return distinct_string
