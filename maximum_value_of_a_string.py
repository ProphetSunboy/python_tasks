class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        """
        The value of an alphanumeric string can be defined as:

            The numeric representation of the string in base 10, if it comprises
            of digits only.
            The length of the string, otherwise.

        Given a list strs of alphanumeric strings, return the maximum value of
        any string in strs.

        LeetCode: Beats 99.9%
        """
        max_val = 0
        num_len = 0

        for s in strs:
            if len(s) >= num_len and s.isdigit():
                num = int(s)

                if num > max_val:
                    max_val = num            
                
            else:
                if len(s) > max_val:
                    max_val = len(s)

        return max_val