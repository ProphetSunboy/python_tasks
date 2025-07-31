class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """Given an integer list arr, return the number of distinct bitwise ORs of all the non-empty sublists of arr.

        The bitwise OR of a sublist is the bitwise OR of each integer in the sublist.
        The bitwise OR of a sublist of one integer is that integer.
        A sublist is a contiguous non-empty sequence of elements within a list.

        Args:
            arr (list[int]): The input list of integers.

        Returns:
            int: The number of distinct bitwise ORs of all non-empty sublists.

        Example:
            >>> subarrayBitwiseORs([0])
            1
            >>> subarrayBitwiseORs([1,1,2])
            3

        Time complexity: O(n^2) in the worst case, where n is the length of arr.
        Space complexity: O(n^2) in the worst case, for storing all possible OR results.
        """
        bitwise_ors = set()
        seen = set()

        for i in range(len(arr)):
            curr_or = arr[i]
            curr_seen = set()

            for num in seen:
                curr_num = num | arr[i]

                bitwise_ors.add(curr_num)
                curr_seen.add(curr_num)

            seen = curr_seen
            bitwise_ors.add(curr_or)
            seen.add(curr_or)

        return len(bitwise_ors)
