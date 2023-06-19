
# seen = []
# unique = []

# for num in nums:
#     if num in seen and num in unique:
#         unique.remove(num)
#     if num not in seen:
#         seen.append(num)
#         unique.append(num)
        
# return sum(unique)


def sumOfUnique(nums) -> int:
    """
    Given an integer array nums return the sum of all the unique
    elements of nums.

    The unique elements of an array are the elements that appear exactly once
    in the array.
    """
    seen = {}

    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1

    return sum(key for key, val in seen.items() if val == 1)