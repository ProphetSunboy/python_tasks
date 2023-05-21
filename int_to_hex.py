class Solution:
    def toHex(self, num: int) -> str:
        '''
        Given an integer num, return a string representing its
        hexadecimal representation.
        For negative integers, two`s complement method is used.
        '''
        return (f'0x{num:x}')[2:] if num >= 0 else f"0x{int('ffffffff', 16) + num + 1:x}"[2:]