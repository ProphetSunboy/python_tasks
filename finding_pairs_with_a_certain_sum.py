class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        """Initialize the FindSumPairs object with two integer lists.

        This class provides methods to:
        - Add values to elements in nums2 list
        - Count pairs (i, j) where nums1[i] + nums2[j] equals a target sum

        Args:
            nums1 (list[int]): First list of integers.
            nums2 (list[int]): Second list of integers.

        Example:
            >>> obj = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
            >>> obj.count(7)
            8
            >>> obj.add(3, 2)
            >>> obj.count(8)
            2

        Time complexity: O(n) where n is the length of nums2 for initialization
        Space complexity: O(n) for storing the frequency dictionary
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.d = dict()

        for num in self.nums2:
            self.d[num] = self.d.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        """Add a positive integer to an element of a given index in the list nums2.

        Args:
            index (int): The index of the element in nums2 to modify.
            val (int): The positive integer value to add to nums2[index].

        Returns:
            None: This method modifies nums2 in-place and returns nothing.

        Example:
            >>> obj = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
            >>> obj.add(3, 2)
            >>> obj.nums2[3]
            4

        Time complexity: O(1) for the addition operation
        Space complexity: O(1) as we only modify existing elements
        """
        self.nums2[index] += val

        self.d[self.nums2[index] - val] -= 1
        self.d[self.nums2[index]] = self.d.get(self.nums2[index], 0) + 1

    def count(self, tot: int) -> int:
        """Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given target sum.

        Args:
            tot (int): The target sum to find pairs for.

        Returns:
            int: The number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

        Example:
            >>> obj = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
            >>> obj.count(7)
            8
            >>> obj.count(8)
            2

        Time complexity: O(n) where n is the length of nums1
        Space complexity: O(1) as we only use a constant amount of extra space
        """
        pairs = 0

        for num in self.nums1:
            if self.d.get(tot - num, 0):
                pairs += self.d[tot - num]

        return pairs
