class Solution:
    def clearStars(self, s: str) -> str:
        res = ""
        l = list(s)

        for i, ch in enumerate(s):
            if ch == "*":
                l[i] = "{"

                smallest = l[i - 1]
                idx = i - 1
                for j in range(i - 2, -1, -1):
                    if l[j] < smallest:
                        smallest = l[j]
                        idx = j

                l[idx] = "{"

        for ch in l:
            if ch != "{":
                res += ch

        return res


a = Solution()
print(a.clearStars("de*"))
