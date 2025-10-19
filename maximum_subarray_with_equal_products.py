class Solution:
    def maxLength(self, nums: List[int]) -> int:
        """
        Given a list of positive integers nums, find the length of the longest sublist
        that is "product equivalent", i.e. for which:

            product(sublist) == lcm(sublist) * gcd(sublist)

        where:
            - product(sublist) is the product of all elements in the sublist
            - lcm(sublist) is the least common multiple of all elements in the sublist
            - gcd(sublist) is the greatest common divisor of all elements in the sublist

        Returns:
            int: The length of the longest product equivalent sublist of nums.

        Example:
            >>> maxLength([2, 3, 6])
            2

        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        longest = 1

        for i in range(len(nums) - 1):
            curr_prod = nums[i] * nums[i + 1]
            curr_gcd = gcd(nums[i], nums[i + 1])
            curr_lcm = lcm(nums[i], nums[i + 1])

            if curr_prod == curr_lcm * curr_gcd and 2 > longest:
                longest = 2

            for j in range(i + 2, len(nums)):
                curr_prod *= nums[j]
                curr_gcd = gcd(curr_gcd, nums[j])
                curr_lcm = lcm(curr_lcm, nums[j])

                if curr_prod == curr_lcm * curr_gcd and j - i + 1 > longest:
                    longest = j - i + 1

        return longest
