class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        """
        Given a 0-indexed list of integers `nums` of length `n`, and two positive
        integers `k` and `dist`.

        The cost of a list is the value of its first element. For example, the cost of
        [1, 2, 3] is 1, while the cost of [3, 4, 1] is 3.

        You need to divide `nums` into `k` disjoint contiguous sublists such that the
        difference between the starting index of the second sublist and the starting index
        of the kth sublist is less than or equal to `dist`. In other words, if you divide
        `nums` into the sublists nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ...,
        nums[ik-1..(n - 1)], then `ik-1 - i1 <= dist`.

        Return the minimum possible sum of the costs of these sublists.

        Args:
            nums (List[int]): The input list.
            k (int): The number of sublists.
            dist (int): The maximum allowed difference between the second and kth sublist starts.

        Returns:
            int: The minimum possible sum of the costs of the selected sublists.

        Example:
            Input: nums = [10, 8, 18, 9], k = 3, dist = 1
            Output: 36

        Time Complexity: O(n^2), where n is the length of nums
        Space Complexity: O(n), due to auxiliary data structures
        """
        n = len(nums)
        m = k - 1

        sl = SortedList(nums[1 : min(n, dist + 2)])
        curr_sum = sum(sl[:m])
        ans = nums[0] + curr_sum

        for i in range(1, n - dist - 1):
            out = nums[i]
            idx = sl.index(out)
            if idx < m:
                curr_sum -= out
                sl.remove(out)
                if len(sl) >= m:
                    curr_sum += sl[m - 1]
            else:
                sl.remove(out)

            in_idx = i + dist + 1
            if in_idx < n:
                val = nums[in_idx]
                sl.add(val)
                idx = sl.index(val)
                if idx < m:
                    curr_sum += val
                    if len(sl) > m:
                        curr_sum -= sl[m]

            if len(sl) >= m:
                ans = min(ans, nums[0] + curr_sum)

        return ans
