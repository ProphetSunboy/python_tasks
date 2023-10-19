class Solution:
    def canThreePartsEqualSum(self, lst: list[int]) -> bool:
        """
        Given a list of integers lst, return True if we can partition the list
        into three non-empty parts with equal sums.

        Formally, we can partition the list if we can find indexes i + 1 < j
        with (lst[0] + lst[1] + ... + lst[i] == lst[i + 1] + lst[i + 2] + ... +
        lst[j - 1] == lst[j] + lst[j + 1] + ... + lst[lst.length - 1])

        :param list[int] lst: list of integers
        :returns bool partition_possible: lst can be partitioned into three
        non-empty parts with equal sums

        Time complexity: O(n)
        Space complexity: O(1)

        LeetCode: Beats 96.24%
        """
        part_sum = sum(lst) / 3

        temp_sum = 0
        partitions = 0
        for i, num in enumerate(lst):
            temp_sum += num

            if temp_sum == part_sum:
                temp_sum = 0
                partitions += 1

                if partitions == 2:
                    break

        if partitions == 2:
            if i + 1 < len(lst):
                temp_sum = part_sum != sum(lst[i + 1 :])
                partitions += 1

        return temp_sum == 0 and partitions == 3
