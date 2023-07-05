class Solution:
    def maxScore(self, s: str) -> int:
        """
        Given a string s of zeros and ones, return the maximum score after
        splitting the string into two non-empty substrings.

        The score after splitting a string is the number of zeros in the left
        substring plus the number of ones in the right substring.

        LeetCode: Beats 98.95%
        """
        # Calculate l_score and r_score.
        l_score, r_score = (1 if s[0] == '0' else 0), s[1:].count('1')

        # Set initial maximum score.
        max_score =  l_score + r_score

        for i in range(1, len(s)-1):
            # Assume, that at the ith iteration we split string at the ith position,
            # so if s[i] == '0', then increment l_score by 1.
            if s[i] == '0':
                l_score += 1

                # l_score + r_score could be bigger than max_score only if
                # the overall score value is increasing.
                if l_score + r_score > max_score:
                    max_score = l_score + r_score
            else:
                # If s[i] == '1' we should decrease r_score by 1
                r_score -= 1 

        return max_score