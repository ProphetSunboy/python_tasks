class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
        The array-form of an integer num is an array representing its digits
        in left to right order.

        For example, for num = 1321, the array form is [1,3,2,1].

        Given num, the array-form of an integer, and an integer k, return
        the array-form of the integer num + k.
        {Leetcode beats 94%}
        """
        while len(num) < len(str(k)):
            num.insert(0, 0)
        summing_position = len(num) - 1
        while k >= 1:
            k, m = divmod(k, 10)
            num[summing_position] += m
            if num[summing_position] > 9:
                num[summing_position] -= 10
                if summing_position == 0:
                    num.insert(0, 1)
                else:
                    i = 1
                    while True:
                        num[summing_position-i] += 1
                        if num[summing_position-i] > 9 and summing_position - i == 0:
                            num[summing_position-i] -= 10
                            num.insert(0, 1)
                            break
                        if num[summing_position-i] > 9:
                            num[summing_position-i] -= 10
                        else:
                            break
                        i += 1
            summing_position -= 1
        return num