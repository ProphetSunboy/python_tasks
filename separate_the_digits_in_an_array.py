# First solution
class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        """Separates each integer in a list into its individual digits while maintaining the original order.

        Given a list of positive integers, returns a new list containing all digits from each integer
        in the same order they appear in the input list.

        Args:
            nums (list[int]): List of positive integers to separate into digits

        Returns:
            list[int]: List of individual digits in the same order as their source integers

        Example:
            >>> separateDigits([13, 25, 83, 77])
            [1, 3, 2, 5, 8, 3, 7, 7]

        Time complexity: O(n * d) - where n is number of integers and d is average number of digits
        Space complexity: O(n * d) - for storing all separated digits

        LeetCode: Beats 100% of submissions
        """
        answer = []

        for num in nums:
            answer.extend(map(int, (list(str(num)))))

        return answer


# Second solution
class Solution:
    def separateDigitsOfInteger(self, num: int) -> list[int]:
        """Separates an integer into its individual digits.

        Given a positive integer, returns a list containing its digits in order from left to right.

        Args:
            num (int): The positive integer to separate into digits

        Returns:
            list[int]: List of digits in order from left to right

        Example:
            >>> separateDigitsOfInteger(123)
            [1, 2, 3]

        Time complexity: O(d) - where d is number of digits in the integer
        Space complexity: O(d) - for storing the digits
        """
        digits = []

        while num > 0:
            digit = num % 10
            num //= 10
            digits.append(digit)

        return digits[::-1]

    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = []

        for num in nums:
            answer.extend(self.separateDigitsOfInteger(num))

        return answer
