class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        """
        Calculates the maximum possible frequency of any element in the list after performing a specified number of operations.

        Each operation allows you to select a unique index in `nums` and add any
        integer within the range [-k, k] to that element. An index can only be selected once.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The maximum value (in both directions) that can be added to a selected element in a single operation.
            numOperations (int): The total number of operations allowed.

        Returns:
            int: The highest frequency achievable for any element after performing all operations.

        Example:
            >>> maxFrequency([1,2,4], 2, 2)
            3  # Example output

        Time Complexity: O(n log n), due to sorting and iterating over possible values.
        Space Complexity: O(n), for storing counts and possible modes.
        """
        nums.sort()
        ans = 0
        num_count = defaultdict(int)
        modes = set()

        def add_mode(value):
            modes.add(value)
            if value - k >= nums[0]:
                modes.add(value - k)
            if value + k <= nums[-1]:
                modes.add(value + k)

        last_num_index = 0
        for i in range(len(nums)):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                add_mode(nums[last_num_index])
                last_num_index = i

        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)
        add_mode(nums[last_num_index])

        for mode in sorted(modes):
            l = bisect.bisect_left(nums, mode - k)
            r = bisect.bisect_right(nums, mode + k) - 1
            if mode in num_count:
                temp_ans = min(r - l + 1, num_count[mode] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)

        return ans
