class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree_min = [0] * (4 * n)
        self.tree_max = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, v):
        if self.lazy[v] != 0:
            self.lazy[2 * v] += self.lazy[v]
            self.tree_min[2 * v] += self.lazy[v]
            self.tree_max[2 * v] += self.lazy[v]
            self.lazy[2 * v + 1] += self.lazy[v]
            self.tree_min[2 * v + 1] += self.lazy[v]
            self.tree_max[2 * v + 1] += self.lazy[v]
            self.lazy[v] = 0

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.tree_min[v] += add
            self.tree_max[v] += add
            self.lazy[v] += add
        else:
            self._push(v)
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
            self.tree_min[v] = min(self.tree_min[2 * v], self.tree_min[2 * v + 1])
            self.tree_max[v] = max(self.tree_max[2 * v], self.tree_max[2 * v + 1])

    def find_leftmost_zero(self, v, tl, tr, r_bound):
        if self.tree_min[v] > 0 or self.tree_max[v] < 0 or tl > r_bound:
            return -1
        if tl == tr:
            return tl
        self._push(v)
        tm = (tl + tr) // 2
        res = self.find_leftmost_zero(2 * v, tl, tm, r_bound)
        if res == -1:
            res = self.find_leftmost_zero(2 * v + 1, tm + 1, tr, r_bound)
        return res


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        """
        Given an integer list nums, returns the length of the longest balanced
        sublist.

        A sublist is balanced if the number of distinct even numbers is equal
        to the number of distinct odd numbers.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The length of the longest balanced sublist.

        Example:
            Input: nums = [2,5,4,3]
            Output: 4

        Time Complexity: O(n log n), due to segment tree operations per element.
        Space Complexity: O(n), for auxiliary data structures.
        """
        n = len(nums)
        st = SegmentTree(n)
        last_seen = {}
        ans = 0

        for r in range(n):
            val = nums[r]
            prev = last_seen.get(val, -1)
            diff = 1 if val % 2 == 0 else -1

            st.update(1, 0, n - 1, prev + 1, r, diff)
            last_seen[val] = r

            l = st.find_leftmost_zero(1, 0, n - 1, r)
            if l != -1:
                ans = max(ans, r - l + 1)

        return ans
