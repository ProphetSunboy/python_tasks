class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Rearranges the given list nums, which consists of 2n elements in the form
        [x1, x2, ..., xn, y1, y2, ..., yn], into the form [x1, y1, x2, y2, ..., xn, yn].

        Args:
            nums (List[int]): List of 2n integers, where the first n elements are x1...xn,
                              and the last n elements are y1...yn.
            n (int): Half the length of nums.

        Returns:
            List[int]: The shuffled list in the pattern [x1, y1, x2, y2, ..., xn, yn].

        Example:
            Input: nums = [2,5,1,3,4,7], n = 3
            Output: [2,3,5,4,1,7]

        Time Complexity: O(n), where n is half the length of nums.
        Space Complexity: O(n), for the result list.

        LeetCode: Beats 92.28% of submissions
        """
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])

        return res
