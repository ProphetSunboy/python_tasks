class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Given a sorted unique integer array nums.

        Return the smallest sorted list of ranges that cover all the numbers in
        the array exactly. That is, each element of nums is covered by exactly
        one of the ranges, and there is no integer x such that x is in one of
        the ranges but not in nums.

        Each range [a,b] in the list is displayed as:

            "a->b" if a != b
            "a" if a == b

        """
        if not nums:
            return []
        res = []
        start = nums[0]
        end = nums[0]
        for i, num in enumerate(nums[1:]):
            if num - end == 1:
                end = num
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f'{str(start)}->{str(end)}')
                start = num
                end = num
        if start == end:
            res.append(str(start))
        else:
            res.append(f'{str(start)}->{str(end)}')
        
        return res