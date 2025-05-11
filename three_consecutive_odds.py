class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        Given an integer list arr, return True if there are three consecutive
        odd numbers in the list. Otherwise, return False.
        """
        counter = 0

        for num in arr:
            if num % 2:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0

        return False
