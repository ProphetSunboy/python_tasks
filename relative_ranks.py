class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        """
        You are given an integer list score of size n, where score[i] is the
        score of the ith athlete in a competition. All the scores are guaranteed
        to be unique.

        The athletes are placed based on their scores, where the 1st place
        athlete has the highest score, the 2nd place athlete has the 2nd highest
        score, and so on. The placement of each athlete determines their rank:

            The 1st place athlete's rank is "Gold Medal".
            The 2nd place athlete's rank is "Silver Medal".
            The 3rd place athlete's rank is "Bronze Medal".
            For the 4th place to the nth place athlete, their rank is their
            placement number (i.e., the xth place athlete's rank is "x").

        Return a list answer of size n where answer[i] is the rank of the ith
        athlete.


        :param list[int] score: results of athletes in competition
        :returns list[str] answer: ranks of the athletes

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.64%
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        answer = [""] * len(score)

        positions = sorted(
            [(val, i) for i, val in enumerate(score)],
            key=lambda item: item[0],
            reverse=True,
        )

        j = 0

        while j < len(score) and j < len(medals):
            answer[positions[j][1]] = medals[j]
            j += 1

        for i in range(len(medals), len(positions)):
            answer[positions[i][1]] = str(i + 1)

        return answer
