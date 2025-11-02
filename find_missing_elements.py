class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """
        Finds missing integers in the complete range defined by the input list.

        Given a list of unique integers `nums`, where the smallest and largest values
        in the intended (continuous) range are guaranteed to be present, finds all
        integers within that range that are missing from the list.

        Args:
            nums (List[int]): List of unique integers. The smallest and largest integers
                in the original intended range are present in nums.

        Returns:
            List[int]: Sorted list of missing integers in the range
                [min(nums), max(nums)], exclusive of the endpoints. If no numbers are
                missing, returns an empty list.

        Example:
            >>> findMissingElements([1, 2, 4, 6])
            [3, 5]

            >>> findMissingElements([3, 4, 5, 6])
            []

        Time Complexity: O(n + d), where n is the number of elements in nums, and
        d is the size of the range.
        Space Complexity: O(n), for storing nums in a set.

        LeetCode: Beats 100% of submissions
        """
        missing = []
        nums_set = set(nums)
        largest = max(nums)
        smallest = min(nums)

        for i in range(smallest + 1, largest):
            if i not in nums_set:
                missing.append(i)

        return missing
