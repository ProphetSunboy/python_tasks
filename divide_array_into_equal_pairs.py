class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        """Determines if a list of 2 * n integers can be divided into n pairs of equal elements.

        Given an integer list `nums` consisting of 2 * n integers, this function checks whether
        it is possible to divide the list into n pairs such that:
            - Each element belongs to exactly one pair.
            - The two elements in each pair are equal.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            bool: True if nums can be divided into n pairs of equal elements, False otherwise.

        Example:
            >>> divideArray([3,2,3,2,2,2])
            True
            >>> divideArray([1,2,3,4])
            False

        Time complexity: O(n), where n is the length of the input list.
        Space complexity: O(n), due to the use of a counter.

        LeetCode: Beats 100% of submissions
        """
        c = Counter(nums)

        for freq in c.values():
            if freq % 2:
                return False

        return True
