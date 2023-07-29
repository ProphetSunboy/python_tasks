class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        """
        Given string s and list widths, return total number of lines and width
        of the last line in pixels.

        You are given a string s of lowercase English letters and an list
        widths denoting how many pixels wide each lowercase English letter is.
        Specifically, widths[0] is the width of 'a', widths[1] is the width of
        'b', and so on.

        You are trying to write s across several lines, where each line is no
        longer than 100 pixels. Starting at the beginning of s, write as many
        letters on the first line such that the total width does not exceed 100
        pixels. Then, from where you stopped in s, continue writing as many
        letters as you can on the second line. Continue this process until you
        have written all of s.

        Return an array result of length 2 where:

            result[0] is the total number of lines.
            result[1] is the width of the last line in pixels.

        LeetCode: Beats 96.86%
        """
        lines = 1
        line_width = 0

        for ch in s:
            l = widths[ord(ch) - 97]

            if l + line_width <= 100:
                line_width += l
            else:
                lines += 1
                line_width = l

        return [lines, line_width]
