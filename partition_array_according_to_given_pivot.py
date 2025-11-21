class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        Rearranges the input list 'nums' according to the following rules:
            1. All elements less than 'pivot' are positioned before all elements
            greater than 'pivot'.
            2. All elements equal to 'pivot' are placed between those less than
            and those greater than 'pivot'.
            3. The relative order of elements within each group (<, ==, >) is
            preserved.

        Args:
            nums (List[int]): The input integer list to be partitioned.
            pivot (int): The pivot value used for partitioning.

        Returns:
            List[int]: The list after rearrangement according to the rules.

        Example:
            Input: nums = [9,12,5,10,14,3,10], pivot = 10
            Output: [9,5,3,10,10,12,14]
                # Elements < 10 come first (9,5,3),
                # Elements == 10 come next (10,10),
                # Elements > 10 come last (12,14);

        Time Complexity: O(n), where n is the number of elements in nums.
        Space Complexity: O(n), for storing output groups.

        LeetCode: Beats 98.30% of submissions
        """
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return less + equal + greater
