class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Finds the duplicated and missing numbers in a set that originally
        contained integers 1 to n.

        The input list 'nums' represents the status of the set after one number
        has been duplicated, resulting in one repeated number and one missing number.

        Args:
            nums (List[int]): The list of integers containing numbers from 1 to n,
            but with one duplicated and one missing.

        Returns:
            List[int]: A list [duplicate, missing], where duplicate is the number
            that occurs twice, and missing is the number absent from nums.

        Example:
            Input: nums = [1,2,2,4]
            Output: [2,3]  # 2 is duplicated, 3 is missing

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), due to the use of a set to track seen numbers.

        LeetCode: Beats 94.98% of submissions
        """
        mismatch = []

        seen = set()
        for num in nums:
            if num in seen:
                mismatch.append(num)
                break
            else:
                seen.add(num)

        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                mismatch.append(i)
                break

        return mismatch
