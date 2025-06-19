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
        total_sum = 0

        for i in range(len(arr)):
            total_sum += arr[i]
            curr_sum = arr[i]

            for j in range(i + 2, len(arr), 2):
                curr_sum += arr[j - 1]
                curr_sum += arr[j]

                total_sum += curr_sum

        return total_sum
