class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        Calculates the x-sum for every sublist of length k in the given list.

        The x-sum of a list is determined as follows:
            1. Count the occurrences of all elements in the list.
            2. Identify the top x most frequent elements. If two elements have the same frequency, the larger element is considered more frequent.
            3. Sum the contributions (value * frequency) of these top x elements to get the x-sum.
            4. If the list contains fewer than x distinct elements, use the sum of the entire list.

        Args:
            nums (List[int]): Input list of integers.
            k (int): Length of each sublist window.
            x (int): Number of most frequent elements to consider for the sum.

        Returns:
            List[int]: List where each element is the x-sum of the corresponding sublist of length k.

        Example:
            >>> findXSum([2, 8, 2, 6, 12], k=3, x=2)
            [12, 14, 18]

        Time Complexity: O(n * k * log k) in the naive approach, but optimized in practice for sliding windows.
        Space Complexity: O(k)

        LeetCode: Beats 91.01% of submissions
        """
        c = Counter(nums[:k])
        answer = []

        for i in range(len(nums) - k + 1):
            x_val = sorted(c.items(), key=lambda item: (item[1], item[0]))[-x:]
            x_sum = 0
            for val, freq in x_val:
                x_sum += val * freq

            answer.append(x_sum)
            if i + k < len(nums):
                c[nums[i]] -= 1
                c[nums[i + k]] += 1

        return answer
