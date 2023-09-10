class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        """
        Given two lists of strings list1 and list2, find the common strings
        with the least index sum.

        A common string is a string that appeared in both list1 and list2.

        A common string with the least index sum is a common string such that if
        it appeared at list1[i] and list2[j] then i + j should be the minimum
        value among all the other common strings.

        Return all the common strings with the least index sum. Return the
        answer in any order.

        :param list[str] list1: list of strings
        :param list[str] list2: list of strings
        :returns list[str] common_s: common strings with the least index sum

        Time complexity: O(n)
        Space complexity: O(n)

        LeetCode: Beats 99.62%
        """
        min_index = 10**4
        common_s = []

        l1_dict = {}
        l2_dict = {}

        for i, l in enumerate(list1):
            l1_dict[l] = i

        for i, l in enumerate(list2):
            l2_dict[l] = i

        for l in list1:
            if l2_dict.get(l, 10**4) == 10**4:
                continue

            index_sum = l1_dict[l] + l2_dict[l]

            if index_sum == min_index:
                common_s.append(l)
            elif index_sum < min_index:
                common_s = [l]
                min_index = index_sum

        return common_s
