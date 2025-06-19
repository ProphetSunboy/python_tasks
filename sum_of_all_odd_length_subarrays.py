# First attempt
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1, 2):
                total_sum += sum(arr[i:j])

        return total_sum


# Second attempt
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        """Returns the sum of all possible odd-length sublists of the input list.

        An odd-length sublist is a contiguous subsequence of the list whose length is odd.

        Args:
            arr (list[int]): List of positive integers.

        Returns:
            int: The sum of all odd-length sublists.

        Examples:
            >>> sumOddLengthSubarrays([1,4,2,5,3])
            58
            >>> sumOddLengthSubarrays([1,2])
            3
            >>> sumOddLengthSubarrays([10,11,12])
            66

        Time complexity: O(N^2), where N is the length of arr.
        Space complexity: O(1).
        """

        for i in range(len(arr)):
            total_sum += arr[i]
            curr_sum = arr[i]

            for j in range(i + 2, len(arr), 2):
                curr_sum += arr[j - 1]
                curr_sum += arr[j]

                total_sum += curr_sum

        return total_sum
