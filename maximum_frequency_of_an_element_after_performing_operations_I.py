class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        Given an integer list `nums`, and two integers `k` and `numOperations`:

        Perform exactly `numOperations` operations. In each operation, select a unique index `i`
        (not selected in previous operations) and add any integer in the range [-k, k] to `nums[i]`.

        After all operations, return the maximum possible frequency of any element in the resulting list.

        Args:
            nums (List[int]): The initial list of integers.
            k (int): The maximum absolute value that can be added to any selected element (per operation).
            numOperations (int): The total number of operations allowed.

        Returns:
            int: The highest frequency of any element achievable after all operations.

        Example:
            >>> maxFrequency([1, 2, 4], 2, 2)
            3

        Time Complexity: O(N log N), where N = len(nums), due to sorting and searching.
        Space Complexity: O(N), for auxiliary structures.
        """
        nums.sort()
        ans = 0
        num_count = {}
        last_num_index = 0
        for i in range(len(nums)):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)

        for i in range(nums[0], nums[-1] + 1):
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)

        return ans
