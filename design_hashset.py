class MyHashSet:
    """
    MyHashSet implements a simple HashSet without using any built-in hash table libraries.

    Methods:
        add(key): Inserts the value 'key' into the HashSet.
        remove(key): Removes the value 'key' from the HashSet if present.
        contains(key): Returns True if 'key' exists in the HashSet, False otherwise.

    Usage Example:
        >>> hashset = MyHashSet()
        >>> hashset.add(1)
        >>> hashset.contains(1)
        True
        >>> hashset.remove(1)
        >>> hashset.contains(1)
        False

    Time Complexity: O(1) average for add, remove, and contains operations.
    Space Complexity: O(N), where N is the number of elements in the HashSet.

    LeetCode: Beats 97.64% of submissions
    """

    def __init__(self):
        self.hashset = {}

    def add(self, key: int) -> None:
        self.hashset[key] = 1

    def remove(self, key: int) -> None:
        if self.hashset.get(key, 0):
            self.hashset.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset
