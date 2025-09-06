class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Given a list `nums` of positive integers and an integer `k`, determine the
        minimum number of operations required to collect all elements from 1 to k.

        In each operation, you remove the last element from `nums` and add it to
        your collection. The goal is to collect at least one of each integer from 1 to k.

        Args:
            nums (List[int]): The input list of positive integers.
            k (int): The target integer; collect all elements from 1 to k.

        Returns:
            int: The minimum number of operations needed to collect all elements 1 through k.

        Example:
            >>> minOperations([3,1,5,4,2], 2)
            4

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(k)

        LeetCode: Beats 100% of submissions
        """
        elems = {i: 1 for i in range(1, k + 1)}
        ops = 0

        while elems and nums:
            val = nums.pop()

            if elems.get(val, 0):
                elems.pop(val)

            ops += 1

        return ops
