def getAverages(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    k_radius = k + k + 1

    if k != 0 and length < k_radius:
        return [-1] * length

    avgs = [-1] * k
    i = k
    summ = sum(nums[i-k:i+k+1])
    k_avg = summ // k_radius
    avgs.append(k_avg)
    i += 1
    
    while length - i > k:
        summ = summ - nums[i-k-1] + nums[i+k]
        k_avg = summ // k_radius
        avgs.append(k_avg)
        i += 1

    avgs += [-1] * (length - i)

    return avgs