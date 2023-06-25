class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        """
        You are given an integer n.
        A 0-indexed integer array nums of lengthn + 1 is generated in the
        following way:

            nums[0] = 0
            nums[1] = 1
            nums[2 * i] = nums[i] when 2 <= 2 * i <= n
            nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

        Return the maximum integer in the array nums.
        """
        if n == 0:
            return 0

        arr = [1]
        max_num = 1
    
        for i in range(1, (n - 1) // 2 + 1):
            if i != 1:
                arr = arr[1:]

            arr.append(arr[0])
            
            odd = arr[0] + arr[1]
            arr.append(odd)

            if odd > max_num:
                max_num = odd

        return max_num