# First attempt
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1, 2):
                total_sum += sum(arr[i:j])

        return total_sum
