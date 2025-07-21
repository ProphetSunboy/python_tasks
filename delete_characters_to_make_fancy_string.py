# First solution
class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        A fancy string is a string where no three consecutive characters are
        equal.

        Given a string s, delete the minimum possible number of characters from
        s to make it fancy.

        Return the final string after the deletion. It can be shown that the
        answer will always be unique.

        LeetCode: Beats 98.67%
        """
        fancy_s = []
        consecutive_count = 0
        curr_consecutive = ""

        for ch in s:
            if consecutive_count < 2 and ch == curr_consecutive:
                consecutive_count += 1
                fancy_s.append(ch)

            if ch != curr_consecutive:
                curr_consecutive = ch
                consecutive_count = 1
                fancy_s.append(ch)

        return "".join(fancy_s)


# Second solution
class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_ch = s[0]
        prev_count = 1
        res = s[0]

        for i in range(1, len(s)):
            if s[i] == prev_ch:
                if prev_count < 2:
                    res += s[i]
                    prev_count += 1
            else:
                prev_ch = s[i]
                res += s[i]
                prev_count = 1

        return res
