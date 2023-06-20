def getAverages(nums: List[int], k: int) -> List[int]:
    """
    You are given a 0-indexed array nums of n integers, and an integer k.

    The k-radius average for a subarray of nums centered at some index i with
    the radius k is the average of all elements in nums between the indices
    i - k and i + k (inclusive). If there are less than k elements before or
    after the index i, then the k-radius average is -1.

    Build and return an array avgs of length n where avgs[i] is the k-radius
    average for the subarray centered at index i.

    The average of x elements is the sum of the x elements divided by x, using
    integer division. The integer division truncates toward zero, which means
    losing its fractional part.

    For example, the average of four elements 2, 3, 1, and 5 is
    (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
    """
    length = len(nums)
    k_radius = k + k + 1

    if k != 0 and length < k_radius:
        return [-1] * length

    # Initialize averages list  
    avgs = [-1] * k

    # Index starts at k, i - k == 0 is starting point of k_radius.
    i = k

    # Count the first subarray average
    summ = sum(nums[i-k:i+k+1])
    k_avg = summ // k_radius
    avgs.append(k_avg)
    i += 1
    
    while length - i > k:
        # It is known that subarrays are consecutive, therefore, to find the
        # sum of the next subarray, it is necessary to subtract
        # the first element of the previous sum and add the next element
        # of the nums array.
        summ = summ - nums[i-k-1] + nums[i+k]
        k_avg = summ // k_radius
        avgs.append(k_avg)
        i += 1

    # If length - i > 0, fill the rest of the list with -1.
    avgs += [-1] * (length - i)

    return avgs