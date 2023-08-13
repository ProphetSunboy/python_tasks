class FasterSolution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        Return the number of unique arithmetic triplets.

        You are given a 0-indexed, strictly increasing integer list nums and a
        positive integer diff. A triplet (i, j, k) is an arithmetic triplet if
        the following conditions are met:

            i < j < k,
            nums[j] - nums[i] == diff, and
            nums[k] - nums[j] == diff.


        :param list[int] nums: strictly increasing integer list
        :param int diff: positive integer
        :returns int counter: number of unique arithmetic triplets


        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 96.41%
        """
        counter = 0
        seen = set()

        for num in nums:
            if num - diff in seen and num - (2 * diff) in seen:
                counter += 1

            seen.add(num)

        return counter


class ConstantMemoryUsageSolution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        Return the number of unique arithmetic triplets.

        You are given a 0-indexed, strictly increasing integer list nums and a
        positive integer diff. A triplet (i, j, k) is an arithmetic triplet if
        the following conditions are met:

            i < j < k,
            nums[j] - nums[i] == diff, and
            nums[k] - nums[j] == diff.


        :param list[int] nums: strictly increasing integer list
        :param int diff: positive integer
        :returns int counter: number of unique arithmetic triplets


        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 91.25%
        """
        counter = 0

        for num in nums:
            if num + diff in nums and num + (2 * diff) in nums:
                counter += 1

        return counter
