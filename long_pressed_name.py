class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        letters_n = 1
        letters_t = 1
        name += "."
        typed += "."

        while i < len(name) - 1:
            if name[i + 1] == name[i]:
                letters_n += 1
                i += 1
                continue

            if typed[j] != name[i]:
                return False

            while j < len(typed) - 1 and typed[j] == typed[j + 1]:
                letters_t += 1
                j += 1

            if letters_t < letters_n:
                return False

            letters_t = 1
            letters_n = 1
            i += 1
            j += 1

        return True


a = Solution()

print(a.isLongPressedName("xnhtq", "xhhttqq"))
