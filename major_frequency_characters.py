class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        """
        Given a string s consisting of lowercase English letters, find the majority frequency group.

        A frequency group for a value k consists of all characters that appear exactly k times in s.
        The majority frequency group has the largest number of distinct characters among all frequency groups.
        If two or more frequency groups tie for the largest size, select the group with the larger frequency k.

        Args:
            s (str): A string consisting of lowercase English letters.

        Returns:
            str: A string containing all characters in the majority frequency group, in any order.

        Example:
            >>> majorityFrequencyGroup("aabbc")
            'ab'    # 'a' and 'b' appear 2 times, that's the largest group.

        Time Complexity: O(n), where n is the length of s.
        Space Complexity: O(n)

        LeetCode: Beats 100% of submissions
        """
        c = Counter(s)
        freq_g = defaultdict(list)

        for ch, freq in c.items():
            freq_g[freq].append(ch)

        major = ""
        major_freq = 0
        k_freq = 0
        for k, ch in freq_g.items():
            if len(ch) > major_freq:
                major_freq = len(ch)
                k_freq = k
                major = "".join(ch)
            elif major_freq == len(ch):
                if k > k_freq:
                    major = "".join(ch)
                    k_freq = k
                elif k == k_freq:
                    major += "".join(ch)

        return major
