# First Solution
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        """
        You are given a string s and an integer t, representing the number of
        transformations to perform. In one transformation, every character in s
        is replaced according to the following rules:

        If the character is 'z', replace it with the string "ab".
        Otherwise, replace it with the next character in the alphabet. For
        example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
        Return the length of the resulting string after exactly t
        transformations.

        Since the answer may be very large, return it modulo 10^9 + 7.
        """
        transformed = ""
        temp = s

        for i in range(t):
            transformed = ""

            for ch in temp:
                if ch == "z":
                    transformed += "a"
                    transformed += "b"
                else:
                    transformed += chr(ord(ch) + 1)

            temp = transformed

        return transformed, len(transformed)


# Second Solution
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        ans = sum(cnt) % mod
        return ans
