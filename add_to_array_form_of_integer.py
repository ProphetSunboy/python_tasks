class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(12000)
        return list(map(int, str(eval(''.join(map(str, num)) + '+' + str(k)))))