class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Given an array of characters letters that is sorted in
        non-decreasing order, and a character target.
        Return the smallest character in letters that is lexicographically
        greater than target. If such a character does not exist, return the
        first character in letters.
        """
        if letters[-1] <= target:
            return letters[0]

        l, r = 0, len(letters)-1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return letters[l]