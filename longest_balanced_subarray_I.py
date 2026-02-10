class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        """
        Given an integer list nums, return the length of the longest balanced
        sublist.

        A sublist is called balanced if the number of distinct even numbers in
        the sublist is equal to the number of distinct odd numbers.

        Args:
            nums (list[int]): The input integer list.

        Returns:
            int: The length of the longest balanced sublist.

        Example:
            Input: nums = [2, 4, 1, 3]
            Output: 4

        Time Complexity: O(n * u), where n is the length of nums and u is the number of unique numbers.
        Space Complexity: O(u), for the maps holding unique evens and odds.
        """
        unique_evens = len(set(x for x in nums if x % 2 == 0))
        unique_odds = len(set(x for x in nums if x % 2 != 0))
        max_k = min(unique_evens, unique_odds)

        ans = 0

        for k in range(1, max_k + 1):
            l = 0
            evens_map = {}
            odds_map = {}

            for r in range(len(nums)):
                val = nums[r]
                if val % 2 == 0:
                    evens_map[val] = evens_map.get(val, 0) + 1
                else:
                    odds_map[val] = odds_map.get(val, 0) + 1

                while len(evens_map) > k or len(odds_map) > k:
                    left_val = nums[l]
                    if left_val % 2 == 0:
                        evens_map[left_val] -= 1
                        if evens_map[left_val] == 0:
                            del evens_map[left_val]
                    else:
                        odds_map[left_val] -= 1
                        if odds_map[left_val] == 0:
                            del odds_map[left_val]
                    l += 1

                if len(evens_map) == k and len(odds_map) == k:
                    ans = max(ans, r - l + 1)

        return ans
