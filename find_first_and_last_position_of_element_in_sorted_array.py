class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Given a list of integers nums sorted in non-decreasing order, find the
        starting and ending position of a given target value.

        If target is not found in the list, return [-1, -1].

        :param list[int] nums: list of integers
        :param int target: target value
        :returns list[int] target_pos: starting and ending position of a given
        target value

        Time complexity: O(logn)
        Space complexity: O(1)

        LeetCode: Beats 98.66%
        """
        l, r = 0, len(nums) - 1
        target_pos = [-1, -1]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                target_pos = [mid, mid]

                for i in range(mid + 1, len(nums)):
                    if nums[i] == target:
                        target_pos[1] += 1
                    else:
                        break

                for i in range(mid - 1, -1, -1):
                    if nums[i] == target:
                        target_pos[0] -= 1
                    else:
                        break

                break

        return target_pos
