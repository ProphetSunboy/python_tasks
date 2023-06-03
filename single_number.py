# First method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears
        twice except for one.
        Return that single one.
        """
        freqs = set()
        for num in nums:
            if num not in freqs:
                freqs.add(num)
            else:
                freqs.remove(num)
        return next(iter(freqs))
    
# Second method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears
        twice except for one.
        Return that single one.
        """
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        return [k for k, v in freqs.items() if v == 1][0]