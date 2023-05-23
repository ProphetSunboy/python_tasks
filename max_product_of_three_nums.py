from math import prod

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find three numbers whose
        product is maximum and return the maximum product.
        """
        sorted_abs = sorted(nums, key=abs)
        elems = sorted_abs[-3:]
        elems_prod = prod(elems)

        g = lambda x: x < 0
        n_neg = sum(map(g, elems))

        if all(map(g, sorted_abs)):
            return prod(sorted_abs[:3])
        if n_neg % 2 == 0:
            return elems_prod
        elif n_neg == 3:
            return prod(elems[-2:]) * max(nums)

        all_pos = elems_prod // min(elems) * max(sorted_abs[:-3])
        two_neg = elems_prod // sorted(elems)[1] * min(sorted_abs[:-3])
        if all_pos >= two_neg:
            return all_pos
        else:
            return two_neg