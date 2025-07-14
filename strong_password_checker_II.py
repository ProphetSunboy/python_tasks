class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        """Determines if the given password is strong based on the following criteria:
            - At least 8 characters long.
            - Contains at least one lowercase letter.
            - Contains at least one uppercase letter.
            - Contains at least one digit.
            - Contains at least one special character from "!@#$%^&*()-+".
            - Does not contain two identical characters in adjacent positions.

        Args:
            password (str): The password string to check.

        Returns:
            bool: True if the password is strong, False otherwise.

        Example:
            >>> strongPasswordCheckerII("IloveCoding2!")
            True
            >>> strongPasswordCheckerII("Me+You--IsMyDream")
            False

        Time complexity: O(n), where n is the length of the password.
        Space complexity: O(1).

        LeetCode: Beats 100% of submissions
        """
        if len(password) < 8:
            return False

        password += " "
        d = {"lower": False, "upper": False, "digit": False, "special": False}

        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
            elif password[i].islower():
                d["lower"] = True
            elif password[i].isupper():
                d["upper"] = True
            elif password[i].isdigit():
                d["digit"] = True
            elif password[i] in "!@#$%^&*()-+":
                d["special"] = True

        return all(d.values())
