class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        The array-form of an integer num is an array representing its digits
        in left to right order.

        For example, for num = 1321, the array form is [1,3,2,1].

        Given num, the array-form of an integer, and an integer k,
        return the array-form of the integer num + k.
        """
        sys.set_int_max_str_digits(12000)
        return list(map(int, str(eval(''.join(map(str, num)) + '+' + str(k)))))