class Fancy:
    """
    An API that generates fancy sequences using append, addAll, and multAll
    operations.

    The Fancy class supports the following methods:
        - __init__(): Initializes the object with an empty sequence.
        - append(val): Appends an integer val to the end of the sequence.
        - addAll(inc): Increments all existing values in the sequence by an
        integer inc.
        - multAll(m): Multiplies all existing values in the sequence by an
        integer m.
        - getIndex(idx): Returns the current value at index idx (0-indexed)
        of the sequence modulo 10^9 + 7. If the index is out of bounds,
        returns -1.

    Example:
        fancy = Fancy()
        fancy.append(2)         # Sequence: [2]
        fancy.addAll(3)         # Sequence: [5]
        fancy.append(7)         # Sequence: [5, 7]
        fancy.multAll(2)        # Sequence: [10, 14]
        fancy.getIndex(0)       # Returns 10

    LeetCode: Beats 96.77% of submissions
    """

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []
        self.mul = 1
        self.add = 0
        self.inv_cache = {}

    def append(self, val: int) -> None:
        if self.mul not in self.inv_cache:
            self.inv_cache[self.mul] = pow(self.mul, self.MOD - 2, self.MOD)

        inv = self.inv_cache[self.mul]
        self.seq.append(((val - self.add) * inv) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        if m == 1:
            return
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1

        return (self.seq[idx] * self.mul + self.add) % self.MOD
