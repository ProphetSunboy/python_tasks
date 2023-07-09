class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        You are given a 0-indexed integer array nums and two integers key and k.
        A k-distant index is an index i of nums for which there exists at least
        one index j such that |i - j| <= k and nums[j] == key.

        Return a list of all k-distant indices sorted in increasing order.
        """
        # Create list of k_distant indices.
        k_distant = []
        
        # Set last checked index.
        last_checked = 0

        for i, num in enumerate(nums):
            # All indices around the key element would be appropriate for k_distant.
            if num == key:
                # Go through indices around key element.
                # Also adjust left border according to the last_checked and
                # make sure, that right border are in the list.
                for j in range(max(last_checked, i-k), min(i+k+1, len(nums))):
                    k_distant.append(j)

                # Update last_checked.
                last_checked = i+k+1
                
                # last_checked >= len(nums) means that all elements were already checked.
                if last_checked >= len(nums):
                    break

        return k_distant