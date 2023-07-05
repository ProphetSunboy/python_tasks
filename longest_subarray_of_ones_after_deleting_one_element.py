
# First method (slower)
class FirstSolution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero_idxs = []
        max_seq = 0

        seq = 0
        for i, num in enumerate(nums):
            if num == 1:
                seq += 1
            else:
                if seq > max_seq:
                    max_seq = seq
                seq = 0
                zero_idxs.append(i)

        if seq > max_seq:
            max_seq = seq

        if not zero_idxs or len(zero_idxs) == 1:
            return len(nums) - 1

        for idx in zero_idxs:
            seq = 0
            i = idx + 1
            j = idx - 1

            if i == len(nums) or j == -1 or nums[i] == 0 or nums[j] == 0:
                continue

            while i != len(nums) and nums[i] != 0:
                seq += 1
                i += 1

            while j != -1 and nums[j] != 0:
                seq += 1
                j -= 1

            if seq > max_seq:
                max_seq = seq

        return max_seq

# Second method (faster)
class SecondSolution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Given a binary array nums, you should delete one element from it.

        Return the size of the longest non-empty subarray containing only 1's
        in the resulting array. Return 0 if there is no such subarray.

        LeetCode: Beats 99.39%
        """
        # Create list of zeros and sums of sequences.
        sum_array = []
        max_seq = 0

        seq = 0
        for i, num in enumerate(nums):
            # Count current subarray of ones
            seq += 1
            
            if num == 0:
                # Substract 1 because subarray sum only includes ones
                seq -= 1

                if seq > 0:
                    sum_array.append(seq)

                    if seq > max_seq:
                        max_seq = seq

                seq = 0
                sum_array.append(0)

        # After all iterations sum_array will look something like this: [0, 2, 0, 1].

        # If there is no zeros in the nums, we should anyway remove one item.
        if seq == len(nums):
            return len(nums) - 1

        # If nums ends with 1, then we should add it after cycle.
        if seq > 0:        
            sum_array.append(seq)

        for i, num in enumerate(sum_array):
            if num == 0 and i != 0 and i != len(sum_array)-1:
                summ = sum_array[i-1] + sum_array[i+1]

                if summ > max_seq:
                    max_seq = summ

        return max_seq