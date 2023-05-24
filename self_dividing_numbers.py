class Solution:
    def is_self_dividing(self, num):
        """
        Given number num check if the num is self-dividing.
        Return True if it is, False otherwise.
        """
        n = num
        while n >= 1:
            n, m = divmod(n, 10)
            if m == 0 or num % m != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        A self-dividing number is a number that isdivisible by every
        digit it contains.

        For example, 128 is a self-dividing number because 128 % 1 == 0,
        128 % 2 == 0, and 128 % 8 == 0.

        A self-dividing number is not allowed to contain the digit zero.

        Given two integers left and right, return a list of all the
        self-dividing numbers in the range [left, right].
        """
        return [num for num in range(left, right+1) if self.is_self_dividing(num)]