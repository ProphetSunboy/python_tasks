class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Removes consecutive anagrams from a list of words.

        Given a 0-indexed list of strings `words`, repeatedly remove any word at index i (where 0 < i < len(words))
        if it is an anagram of the previous word (words[i-1]). Continue this process until no such adjacent anagrams remain.

        An anagram is a word formed by rearranging the letters of another word using all original letters exactly once.

        Args:
            words (List[str]): List of lowercase English words.

        Returns:
            List[str]: The list after removing all consecutive anagrams.

        Example:
            >>> removeAnagrams(["abba","baba","bbaa","cd","cd"])
            ['abba', 'cd']

        Time Complexity: O(n * k log k), where n is the number of words and k is the maximum word length (for sorting).
        Space Complexity: O(n * k), for storing sorted representations of words.

        LeetCode: Beats 100% of submissions
        """
        words_letters = [sorted(word) for word in words]
        stack = [0]

        for i in range(1, len(words)):
            if words_letters[i] != words_letters[stack[-1]]:
                stack.append(i)

        return [words[i] for i in stack]
