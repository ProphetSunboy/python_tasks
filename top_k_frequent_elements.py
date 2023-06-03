class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most
        frequent elements.
        """
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        return [key for key, v in sorted(freqs.items(), key=lambda x: x[1])][-k:]