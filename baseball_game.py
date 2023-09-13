class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Return the sum of all the scores on the record after applying all the
        operations.

        You are keeping the scores for a baseball game with strange rules. At
        the beginning of the game, you start with an empty record.

        You are given a list of strings operations, where operations[i] is the
        ith operation you must apply to the record and is one of the following:

            An integer x.
                Record a new score of x.
            '+'.
                Record a new score that is the sum of the previous two scores.
            'D'.
                Record a new score that is the double of the previous score.
            'C'.
                Invalidate the previous score, removing it from the record.


        :param list[str] operations: strings operations
        :returns int score: sum of all the scores on the record after applying
        all the operations

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 97.45%
        """
        scores = []
        score = 0

        for oper in operations:
            if oper == "C":
                val = scores.pop()
                score -= val
            elif oper == "D":
                scores.append(scores[-1] * 2)
                score += scores[-1]
            elif oper == "+":
                scores.append(scores[-1] + scores[-2])
                score += scores[-1]
            else:
                scores.append(int(oper))
                score += scores[-1]

        return score
