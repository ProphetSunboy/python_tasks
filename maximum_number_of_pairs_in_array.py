class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        """Given a 0-indexed integer list nums, repeatedly form pairs by removing two equal integers from nums.
        Each operation removes both integers, forming a pair. Perform this operation as many times as possible.

        Args:
            nums (list[int]): List of integers to form pairs from.

        Returns:
            list[int]: A list of size 2 where:
                - answer[0] is the number of pairs formed,
                - answer[1] is the number of leftover integers in nums after all possible pairs are formed.

        Example:
            >>> numberOfPairs([1,3,2,1,3,2,2])
            [3, 1]  # Three pairs can be formed: (1,1), (3,3), (2,2), with one 2 left over.

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(n), for storing the frequency count.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)
        answer = [0, 0]

        for num, freq in c.items():
            answer[0] += freq // 2
            answer[1] += freq - freq // 2 * 2

        return answer
