class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
        Given a list of integers nums, repeatedly replace any two adjacent non-coprime
        numbers with their least common multiple (LCM) until no such pairs remain.

        Two numbers are non-coprime if their greatest common divisor (GCD) is greater than 1.

        The process is as follows:
            1. Find any two adjacent numbers in nums that are non-coprime.
            2. Replace them with their LCM.
            3. Repeat until no adjacent non-coprime pairs exist.

        The final list is unique regardless of the order of replacements.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[int]: The modified list after all possible replacements.

        Example:
            >>> replaceNonCoprimes([6,4,3,2,7,6,2])
            [12,7,6]

        Constraints:
            - The values in the final list are less than or equal to 10^8.

        Time Complexity: O(n log M), where n is the length of nums and M is the maximum value in nums.
        Space Complexity: O(n)
        """
        nums = nums[::-1]
        res = []

        while len(nums) >= 2:
            if gcd(nums[-1], nums[-2]) > 1:
                curr_lcm = lcm(nums[-1], nums[-2])
                nums.pop()
                nums.pop()
                nums.append(curr_lcm)
                if res and gcd(res[-1], nums[-1]) > 1:
                    nums.append(res.pop())
            else:
                res.append(nums.pop())

        return res + nums[::-1]
