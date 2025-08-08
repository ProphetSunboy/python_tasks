class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        """
        Given an integer list nums where each element is either a positive integer or -1,
        return a list where for each -1 in nums, you append the k-th most recently
        seen positive integer to the result, where k is the number of consecutive
        -1s up to and including the current one.
        If there are not enough previously seen positive integers, append -1 instead.

        Approach:
            - Maintain a list `seen` to store positive integers encountered so far.
            - Iterate through nums:
                - If the current number is positive, add it to `seen` and reset the consecutive -1 counter.
                - If the current number is -1, increment the consecutive -1 counter (k).
                    - If k <= len(seen), append the k-th last element from `seen` to the result.
                    - Otherwise, append -1.

        Args:
            nums (list[int]): List of integers, each either positive or -1.

        Returns:
            list[int]: List containing the last visited integer for each -1 in nums.

        Example:
            >>> =lastVisitedIntegers([1, 2, -1, -1, -1])
            [2, 1, -1]

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        seen = []
        ans = []
        k = 0

        for num in nums:
            if num > 0:
                seen.append(num)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[-k])
                else:
                    ans.append(-1)

        return ans
