class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Given a list of integers representing fruit trees in a row (fruits), where fruits[i] is the type of fruit on the i-th tree,
        find the length of the longest contiguous sublist containing at most two distinct types of fruit.

        You have two baskets, each of which can only hold a single type of fruit, but can hold any quantity.
        Starting from any tree, you must pick exactly one fruit from each tree as you move to the right, stopping when you encounter a third type.

        Args:
            fruits (list[int]): The types of fruit on each tree in the row.

        Returns:
            int: The maximum number of fruits that can be picked following the rules.

        Example:
            >>> totalFruit([1,2,1])
            3
            >>> totalFruit([0,1,2,2])
            3
            >>> totalFruit([1,2,3,2,2])
            4

        Time complexity: O(n), where n is the length of fruits.
        Space complexity: O(1).
        """
        max_fruits = 0
        curr = set([fruits[0]])
        curr_fruits = 0
        i = 0
        j = 0
        while i < len(fruits):
            if fruits[i] in curr:
                curr_fruits += 1
                i += 1
            elif fruits[i] not in curr and len(curr) < 2:
                curr.add(fruits[i])
                j = i
                curr_fruits += 1
                i += 1
            else:
                curr = set([fruits[j]])
                if curr_fruits > max_fruits:
                    max_fruits = curr_fruits
                curr_fruits = 0
                i = j
                j = 0

        if curr_fruits > max_fruits:
            max_fruits = curr_fruits

        return max_fruits
