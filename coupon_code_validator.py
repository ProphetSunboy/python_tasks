class Solution:
    def validateCoupons(
        self, code: list[str], businessLine: list[str], isActive: list[bool]
    ) -> list[str]:
        """
        Validates and returns a list of coupon codes that meet specific criteria.

        You are given three lists of length n:
            - code: List of strings representing coupon identifiers.
            - businessLine: List of strings representing the business category of each coupon.
            - isActive: List of booleans indicating whether each coupon is currently active.

        A coupon is considered valid if all of the following conditions are met:
            1. code[i] is non-empty and contains only alphanumeric characters (a-z, A-Z, 0-9) or underscores (_).
            2. businessLine[i] is one of: "electronics", "grocery", "pharmacy", "restaurant".
            3. isActive[i] is True.

        Returns a list of valid coupon codes, sorted first by businessLine in the order:
        "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical order within each category.

        Args:
            code (list[str]): List of coupon codes.
            businessLine (list[str]): List of business categories for each coupon.
            isActive (list[bool]): List indicating if each coupon is active.

        Returns:
            list[str]: Sorted list of valid coupon codes.

        Example:
            >>> validateCoupons(
            ...     ["A1", "B2", "C_3", "D4"],
            ...     ["electronics", "grocery", "pharmacy", "restaurant"],
            ...     [True, False, True, True]
            ... )
            ['A1', 'C_3', 'D4']

        Time Complexity: O(n log n), where n is the number of coupons (due to sorting).
        Space Complexity: O(n), for storing valid coupons.

        LeetCode: Beats 94.06% of submissions
        """
        valid = []
        business_cat = ["electronics", "grocery", "pharmacy", "restaurant"]

        for i in range(len(code)):
            if isActive[i]:
                if businessLine[i] in business_cat:
                    if code[i] and all(c.isalnum() or c == "_" for c in code[i]):
                        valid.append((code[i], businessLine[i]))

        return [val[0] for val in sorted(valid, key=lambda x: (x[1], x[0]))]
