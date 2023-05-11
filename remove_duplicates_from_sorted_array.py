def removeDuplicates(self, nums: List[int]) -> int:
    '''
    Given an integer array nums sorted in non-decreasing order,
    removes the duplicates in-place such that each unique element
    appears only once.
    The relative order of the elements remains the same.
    Return the number of unique elements in nums.
    '''
    for i in range(len(nums)-1, 0, -1):
        if nums[i] in nums[:i]: nums.pop(i)
    return len(nums)