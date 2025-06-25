class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        """Merges two 2D integer lists by summing values with the same id.

        Each input list, nums1 and nums2, contains sublists of the form [id, value], where:
            - Each id is unique within its list.
            - Both lists are sorted in ascending order by id.

        The merged result contains all unique ids from both lists, sorted in ascending order.
        For each id, its value in the result is the sum of its values from nums1 and nums2.
        If an id is missing from one list, its value from that list is considered 0.

        Args:
            nums1 (list[list[int]]): First list of [id, value] pairs.
            nums2 (list[list[int]]): Second list of [id, value] pairs.

        Returns:
            list[list[int]]: Merged list of [id, summed_value] pairs, sorted by id.

        Example:
            >>> mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]])
            [[1, 6], [2, 3], [3, 2], [4, 6]]

        LeetCode: Beats 100% of submissions
        """
        res = []
        res_dict = dict()

        for key, val in nums1:
            res_dict[key] = res_dict.get(key, 0) + val

        for key, val in nums2:
            res_dict[key] = res_dict.get(key, 0) + val

        for key, val in sorted(res_dict.items(), key=lambda x: x[0]):
            res.append([key, val])

        return res
