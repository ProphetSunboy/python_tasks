class FirstSolution:
    def dominantIndex(self, nums: list[int]) -> int:
        """
        You are given an integer array nums where the largest integer is unique.

        Determine whether the largest element in the array is at least twice as
        much as every other number in the array. If it is, return the index of
        the largest element, or return -1 otherwise.

        LeeCode: Beats 94.20%
        """
        max_num = 0
        k = -1

        for i, num in enumerate(nums):
            if num >= max_num * 2:
                max_num = num
                k = i
            elif num * 2 > max_num:
                max_num = [num, max_num][max_num > num]
                k = -1

        return k

class SecondSolution:
    def dominantIndex(self, nums: list[int]) -> int:
        """
        LeetCode: Beats 90.14%
        """
        max_num = 0
        max_i = 0
    
        sec_max = 0
        
        for i, num in enumerate(nums):
            if num > max_num:
                sec_max = max_num
                max_num, max_i = num, i
            elif num > sec_max:
                sec_max = num

        return max_i if max_num >= sec_max * 2 else -1