class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        """
        Given a 0-indexed integer list nums and an integer key (guaranteed to be present in nums),
        find the integer target that most frequently appears immediately after key in nums.

        For every unique integer target in nums, count the number of times target immediately follows an occurrence of key.
        That is, count the number of indices i such that:
            0 <= i <= len(nums) - 2,
            nums[i] == key,
            nums[i + 1] == target

        Return the target with the maximum count. It is guaranteed that the answer is unique.

        Args:
            nums (List[int]): The input list of integers.
            key (int): The integer whose following value is to be analyzed.

        Returns:
            int: The integer that most frequently follows key in nums.

        Example:
            >>> mostFrequent([1,100,200,1,100], 1)
            100
            >>> mostFrequent([2,2,2,2,3], 2)
            2

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(U), where U is the number of unique integers in nums.

        LeetCode: Beats 100% of submissions
        """
        targets = defaultdict(int)

        for i in range(1, len(nums)):
            if nums[i - 1] == key:
                targets[nums[i]] += 1

        return max(targets.items(), key=lambda item: item[1])[0]
