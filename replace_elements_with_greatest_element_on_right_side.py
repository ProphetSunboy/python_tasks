# First Solution crate additional list
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """
        Given a list arr, replace every element in that list with the greatest
        element among the elements to its right, and replace the last element
        with -1.

        After doing so, return the list.


        LeetCode BEat 98.21%
        """
        l = [-1]
        greatest = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            l.append(greatest)

            if arr[i] > greatest:
                greatest = arr[i]

        l.reverse()

        return l


# Second solution replace elements in-place
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > greatest:
                arr[i], greatest = greatest, arr[i]
            else:
                arr[i] = greatest

        return arr
