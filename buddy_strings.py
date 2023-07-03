class Solution:
    def buddy_strings(self, s: str, goal: str) -> bool:
        """
        Given two strings s and goal, return True if you can swap two letters
        in s so the result is equal to goal, otherwise, return False.

        Swapping letters is defined as taking two indices i and j (0-indexed)
        such that i != j and swapping the characters at s[i] and s[j].

        For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

        
        LeetCode: Beats 99.90%
        """
        # If lengths aren't equal it's obvious that you can't' achieve equality by swapping letters.
        if len(s) != len(goal):
            return False
        # If strings are equal but all characters of s are unique: 'abcd' == 'abcd' you can't swap to equality.
        if s == goal and len(set(s)) == len(s):
            return False
        # After previous condition we know that strings are equal, and at least
        # 2 characters in s are repeated: 'aab' == 'aab', you can swap 2 repeated characters.
        if s == goal:
            return True

        # Create swapping table.
        swap_idxs = []

        for i, x in enumerate(zip(s, goal)):
            # Check if elems in ith position are different.
            if x[0] != x[1]:
                # If so, add index to swapping table.
                swap_idxs.append(i)
                # We can't swap 2 characters in string to make them equal if there are more than 2 indexes.
                if len(swap_idxs) > 2:
                    return False
                
        # If 1 index is different, but all other are equal, return False
        if len(swap_idxs) != 2:
            return False

        # We already know that all elems of s are equal to goal, except those in swap_idxs.
        # So if swap_idxs[0] of s is equal to swap_idxs[1] of goal and swap_idxs[1]
        # of s is equal to swap_idxs[0] of goal, then we can swap 2 characters and achieve equality.
        if s[swap_idxs[0]] == goal[swap_idxs[1]] and s[swap_idxs[1]] == goal[swap_idxs[0]]:
            return True

        # If any of those elements are not equal, return False.
        return False