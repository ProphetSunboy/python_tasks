class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        """
        Computes the distinct difference list for a given list of integers.

        The distinct difference list `diff` of a 0-indexed list `nums` of length `n` is defined as:
            diff[i] = (number of distinct elements in nums[0..i]) - (number of distinct elements in nums[i+1..n-1])

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            list[int]: The distinct difference list.

        Example:
            >>> distinctDifferenceArray([1,2,3,4,5])
            [-3,-1,1,3,5]

        Time Complexity: O(n)
        Space Complexity: O(n)

        LeetCode: Beats 91.49% of submissions
        """
        pref = Counter(nums[0:1])
        suff = Counter(nums[1:])
        diff = [len(pref) - len(suff)]

        for i in range(1, len(nums)):
            pref[nums[i]] += 1
            suff[nums[i]] -= 1
            if suff[nums[i]] == 0:
                suff.pop(nums[i])

            diff.append(len(pref) - len(suff))

        return diff
