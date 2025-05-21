# First attempt:
class Solution:
    def sortString(self, s: str) -> str:
        """
        :param str s: string to reorder
        :returns str: reordered string according to the algorithm

        Time complexity: O(n^2) where n is length of input string
        Space complexity: O(n) for storing the list and result string
        """
        l = list(s)
        l.sort()
        res = ""

        while l:
            res += l.pop(0)

            i = 0
            while i < len(l):
                if l[i] > res[-1]:
                    res += l.pop(i)
                    i -= 1

                i += 1

            if l:
                res += l.pop()

            i = len(l) - 1
            while i > -1:
                if l[i] < res[-1]:
                    res += l.pop(i)

                i -= 1

        return res


# Second attempt:
class Solution:
    def sortString(self, s: str) -> str:
        """
        You are given a string s. Reorder the string using the following algorithm:

        Remove the smallest character from s and append it to the result.
        Remove the smallest character from s that is greater than the last appended character, and append it to the result.
        Repeat step 2 until no more characters can be removed.
        Remove the largest character from s and append it to the result.
        Remove the largest character from s that is smaller than the last appended character, and append it to the result.
        Repeat step 5 until no more characters can be removed.
        Repeat steps 1 through 6 until all characters from s have been removed.
        If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

        Return the resulting string after reordering s using this algorithm.

        :param str s: string to reorder
        :returns str: reordered string

        Time complexity: O(n log n)
        Space complexity: O(n)

        LeetCode: Beats 93.25%
        """
        # Convert string to list of characters and count frequencies
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        result = []

        # Continue until all characters are used
        while char_count:
            # Step 1-3: Append characters in ascending order
            for c in sorted(char_count.keys()):
                result.append(c)
                char_count[c] -= 1
                if char_count[c] == 0:
                    del char_count[c]

            if not char_count:
                break

            # Step 4-6: Append characters in descending order
            for c in sorted(char_count.keys(), reverse=True):
                result.append(c)
                char_count[c] -= 1
                if char_count[c] == 0:
                    del char_count[c]

        return "".join(result)
