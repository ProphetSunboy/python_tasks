class FasterSolution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """
        Given a list of integers nums, half of the integers in nums are odd,
        and the other half are even.

        Sort the list so that whenever nums[i] is odd, i is odd, and whenever
        nums[i] is even, i is even.

        Return any answer list that satisfies this condition.

        :param list[int] nums: list of integers
        :returns list[int] res: list with odd elements at odd index and even
        elements at even index

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.19%
        """
        res = [0] * len(nums)
        even, odd = 0, 1

        for num in nums:
            if num % 2:
                res[odd] = num
                odd += 2
            else:
                res[even] = num
                even += 2

        return res


class SlowerSolution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evens = []
        odds = []

        for num in nums:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)

        return [odds.pop() if i % 2 else evens.pop() for i in range(len(nums))]
