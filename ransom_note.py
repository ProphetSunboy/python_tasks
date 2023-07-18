class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given two strings ransomNote and magazine, return True if ransomNote can
        be constructed by using the letters from magazine and False otherwise.

        Each letter in magazine can only be used once in ransomNote.
        """
        if len(ransomNote) > len(magazine):
            return False

        set_a = set(ransomNote)
        set_b = set(magazine)

        if len(set_a) == len(set_b) and set_a - set_b == set():
            return True
        
        rans_map = {}
        mag_map = {}

        for ch in ransomNote:
            rans_map[ch] = rans_map.get(ch, 0) + 1

        for ch in magazine:
            mag_map[ch] = mag_map.get(ch, 0) + 1

        for ch, freqs in rans_map.items():
            if freqs > mag_map.get(ch, 0):
                return False

        return True