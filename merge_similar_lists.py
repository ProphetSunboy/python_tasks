class Solution:
    def mergeSimilarItems(
        self, items1: list[list[int]], items2: list[list[int]]
    ) -> list[list[int]]:
        """
        You are given two 2D integer lists, items1 and items2, representing two
        sets of items. Each array items has the following properties:

            items[i] = [valuei, weighti] where valuei represents the value and
            weighti represents the weight of the ith item.
            The value of each item in items is unique.

        Return a 2D integer array ret where ret[i] = [valuei, weighti], with
        weighti being the sum of weights of all items with value valuei.

        Note: ret should be returned in ascending order by value.

        :param list[list[int]] items1: 2D integer list with value and weight
        :param list[list[int]] items1: 2D integer list with value and weight
        :returns list[list[int]] ret: sum of weights of all items with value valuei

        Time complexity: O((n+m)log(n+m))
        Space complexity: O(1)

        LeetCode: Beats 99.18%
        """
        values = {}
        for v, w in items1:
            values[v] = w

        for v, w in items2:
            values[v] = values.get(v, 0) + w

        ret = []
        for v, w in values.items():
            ret.append([v, w])

        return sorted(ret, key=lambda item: item[0])
