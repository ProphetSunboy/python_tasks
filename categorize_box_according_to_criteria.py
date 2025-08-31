class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        """
        Categorizes a box based on its dimensions and mass.

        A box is classified as:
        - "Bulky" if any dimension (length, width, or height) is greater than or equal to 10^4,
          or if the volume (length * width * height) is greater than or equal to 10^9.
        - "Heavy" if its mass is greater than or equal to 100.

        The category returned is:
        - "Both" if the box is both "Bulky" and "Heavy".
        - "Bulky" if the box is "Bulky" but not "Heavy".
        - "Heavy" if the box is "Heavy" but not "Bulky".
        - "Neither" if the box is neither "Bulky" nor "Heavy".

        Args:
            length (int): The length of the box.
            width (int): The width of the box.
            height (int): The height of the box.
            mass (int): The mass of the box.

        Returns:
            str: The category of the box ("Both", "Bulky", "Heavy", or "Neither").

        Example:
            >>> categorizeBox(10000, 10000, 10000, 100)
            'Both'

        Time Complexity: O(1)
        Space Complexity: O(1)

        LeetCode: Beats 100% of submissions
        """
        if (
            length >= 10**4
            or width >= 10**4
            or height >= 10**4
            or length * width * height >= 10**9
        ):
            if mass >= 100:
                return "Both"
            else:
                return "Bulky"
        elif mass >= 100:
            return "Heavy"

        return "Neither"
