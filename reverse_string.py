class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Return reversed string. The input string is given as an
        array of characters s.
        """
        length = len(s) - 1

        for i in range(len(s) // 2):
            temp = s[i] 
            s[i] = s[length]
            s[length] = temp
            length -= 1