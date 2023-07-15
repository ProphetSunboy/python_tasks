class Solution:
    def interpret(self, command: str) -> str:
        """
        You own a Goal Parser that can interpret a string command. The command
        consists of an alphabet of "G", "()" and/or "(al)" in some order.
        The Goal Parser will interpret "G" as the string "G", "()" as the string
        "o", and "(al)" as the string "al". The interpreted strings are then
        concatenated in the original order.

        Given the string command, return the Goal Parser's interpretation of
        command.
        
        LeetCode: Beats 95.92%
        """
        res = ''
        
        for i in range(len(command)):
            if command[i] == '(':
                if command[i+1] == ')':
                    res += 'o'
                    i += 1
                else:
                    res += 'al'
                    i += 3
            elif command[i] == 'G':
                res += 'G'

        return res