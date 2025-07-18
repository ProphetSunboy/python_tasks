class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        """Counts the number of beautiful pairs in a 0-indexed integer list `nums`.

        A pair of indices (i, j) with 0 <= i < j < len(nums) is called beautiful if
        the first digit of nums[i] and the last digit of nums[j] are coprime
        (i.e., gcd(first_digit(nums[i]), last_digit(nums[j])) == 1).

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The total number of beautiful pairs in nums.

        Example:
            >>> countBeautifulPairs([2, 5, 1, 4])
            5

        Time complexity: O(n^2) in the naive approach, but this implementation is optimized.
        Space complexity: O(n)

        LeetCode: Beats 99.07% of submissions
        """
        seen = dict()
        pairs = 0

        for num in nums:
            f_digit = int(str(num)[0])
            l_digit = num % 10

            for n, count in seen.items():
                if math.gcd(n, l_digit) == 1:
                    pairs += count

            seen[f_digit] = seen.get(f_digit, 0) + 1

        return pairs
