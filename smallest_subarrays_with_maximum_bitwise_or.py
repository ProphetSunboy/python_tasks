class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        """Given a 0-indexed list nums of length n consisting of non-negative integers,
        for each index i (0 <= i < n), find the length of the smallest non-empty sublist
        starting at i whose bitwise OR is equal to the maximum possible bitwise OR
        for any sublist starting at i.

        More formally, for each i, let Bij be the bitwise OR of the sublist nums[i...j].
        Find the smallest length l such that the bitwise OR of nums[i:i+l] equals
        the maximum value of Bij for all j in [i, n-1].

        Args:
            nums (list[int]): The input list of non-negative integers.

        Returns:
            list[int]: List answer where answer[i] is the length of the minimum sublist starting at i with the maximum bitwise OR.

        Example:
            >>> smallestSubarrays([1,0,2,1,3])
            [3,3,2,2,1]

        Time complexity: O(n^2)
        Space complexity: O(n), for the output list.
        """
        max_or = nums[-1]
        answer = deque([1])

        for i in range(len(nums) - 2, -1, -1):
            max_or |= nums[i]

            curr_or = nums[i]
            for j in range(i, len(nums)):
                curr_or |= nums[j]

                if curr_or == max_or:
                    answer.appendleft(j - i + 1)
                    break

        return list(answer)
