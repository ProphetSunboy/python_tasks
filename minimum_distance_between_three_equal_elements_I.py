class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        Finds the minimum possible distance of a "good" tuple in the given integer list.

        A tuple (i, j, k) of 3 distinct indices is considered "good" if nums[i] == nums[j] == nums[k].
        The distance of such a tuple is defined as abs(i - j) + abs(j - k) + abs(k - i).

        Args:
            nums (List[int]): An integer list.

        Returns:
            int: The minimum distance among all good tuples, or -1 if no such tuple exists.

        Example:
            Input: nums = [1,2,1,1,3]
            Output: 6

        Time Complexity: O(n), where n is the length of nums.
        Space Complexity: O(n), due to the use of a dictionary to store indices.

        LeetCode: Beats 100% of submissions
        """
        elems = {}
        min_dist = float("infinity")

        def get_distance(curr_list):
            curr_dist = (
                abs(curr_list[0] - curr_list[1])
                + abs(curr_list[1] - curr_list[2])
                + abs(curr_list[2] - curr_list[0])
            )

            return curr_dist

        for i, num in enumerate(nums):
            if elems.get(num, 0) == 0:
                elems[num] = [i]
            else:
                if len(elems[num]) < 3:
                    elems[num].append(i)
                else:
                    elems[num].pop(0)
                    elems[num].append(i)

                if len(elems[num]) == 3:
                    min_dist = min(get_distance(elems[num]), min_dist)

        if min_dist == float("infinity"):
            min_dist = -1

        return min_dist
