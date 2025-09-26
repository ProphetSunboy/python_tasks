class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        Determines if one list can be transformed into another by reversing any number of sublists.

        Given two integer lists of equal length, target and arr, you can reverse
        any non-empty sublist of arr any number of times.
        Return True if arr can be made equal to target, otherwise return False.

        Args:
            target (List[int]): The target list.
            arr (List[int]): The list to transform.

        Returns:
            bool: True if arr can be transformed into target, False otherwise.

        Example:
            >>> canBeEqual([1,2,3,4], [2,4,1,3])
            True

        Time Complexity: O(N), where N is the length of the lists.
        Space Complexity: O(N), for the frequency counters.

        LeetCode: Beats 100% of submissions
        """
        c_t = Counter(target)
        c_a = Counter(arr)

        return c_t == c_a
