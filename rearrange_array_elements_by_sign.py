class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Rearranges an even-length list so that elements alternate in sign,
        starting with a positive integer, and preserves the original relative
        order of positive and negative numbers.

        Args:
            nums (List[int]): A 0-indexed integer list with equal numbers of
            positive and negative integers.

        Returns:
            List[int]: The rearranged list where every consecutive pair has
            opposite signs, and the relative ordering of positives and
            negatives is preserved.

        Example:
            Input: nums = [3,1,-2,-5,2,-4]
            Output: [3,-2,1,-5,2,-4]

        Time Complexity: O(N), where N is the length of nums.
        Space Complexity: O(N), for the output list.

        LeetCode: Beats 97.44% of submissions
        """
        res = [0] * len(nums)
        pos_idx = 0
        neg_idx = 1

        for num in nums:
            if num > 0:
                res[pos_idx] = num
                pos_idx += 2
            else:
                res[neg_idx] = num
                neg_idx += 2

        return res
