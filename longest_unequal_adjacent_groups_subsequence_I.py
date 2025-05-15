class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        You are given a string list words and a binary list groups both of
        length n, where words[i] is associated with groups[i].

        Your task is to select the longest alternating subsequence from words.
        A subsequence of words is alternating if for any two consecutive strings
        in the sequence, their corresponding elements in the binary list groups
        differ. Essentially, you are to choose strings such that adjacent
        elements have non-matching corresponding bits in the groups array.

        Formally, you need to find the longest subsequence of a list of indices
        [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that
        groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the
        words corresponding to these indices.

        Return the selected subsequence. If there are multiple answers, return
        any of them.

        Note: The elements in words are distinct.

        LeetCode Beats 100%
        """
        longest = []

        curr_g = False
        for i, word in enumerate(words):
            if groups[i] == curr_g:
                longest.append(word)
                curr_g = not curr_g

        curr_g = True
        local_longest = []
        for i, word in enumerate(words):
            if groups[i] == curr_g:
                local_longest.append(word)
                curr_g = not curr_g

        return longest if len(longest) > len(local_longest) else local_longest
