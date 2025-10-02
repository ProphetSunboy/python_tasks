class OrderedStream:
    """
    OrderedStream class maintains a stream of (idKey, value) pairs, where idKey is an integer from 1 to n and value is a string.
    Pairs can arrive in any order, but no two pairs have the same idKey.

    After each insertion, the stream returns the largest possible chunk (list) of values in order, starting from the current pointer.
    The concatenation of all returned chunks will result in the values sorted by idKey.

    Methods:
        __init__(n: int):
            Initializes the stream to accept n values.

        insert(idKey: int, value: str) -> List[str]:
            Inserts the (idKey, value) pair into the stream.
            Returns the largest contiguous chunk of values in order starting from the current pointer.

    Example:
        >>> os = OrderedStream(5)
        >>> os.insert(3, "cc")
        []
        >>> os.insert(1, "aa")
        ['aa']
        >>> os.insert(2, "bb")
        ['bb', 'cc']
        >>> os.insert(5, "ee")
        []
        >>> os.insert(4, "dd")
        ['dd', 'ee']

    Time Complexity:
        Each insert operation is O(n) in the worst case (if a large chunk is returned), but typically O(1) amortized.

    Space Complexity:
        O(n), where n is the number of values in the stream.

    LeetCode: Beats 97.62% of submissions
    """

    def __init__(self, n: int):
        self.stream = [0] * (n + 1)
        self.curr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        if idKey != self.curr:
            return []

        i = self.curr

        while self.curr < len(self.stream) and self.stream[self.curr]:
            self.curr += 1

        return self.stream[i : self.curr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
