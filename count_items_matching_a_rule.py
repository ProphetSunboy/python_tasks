class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        """Counts the number of items that match a given rule.

        Each item is represented as [type, color, name]. A rule consists of a ruleKey
        ("type", "color", or "name") and a ruleValue. An item matches if its value
        at the ruleKey's position equals the ruleValue.

        Args:
            items (list[list[str]]): List of items, where each item is [type, color, name]
            ruleKey (str): The attribute to check ("type", "color", or "name")
            ruleValue (str): The value to match against

        Returns:
            int: Number of items matching the rule

        Example:
            >>> countMatches([["phone","blue","pixel"],["computer","silver","lenovo"]], "color", "silver")
            1

        Time complexity: O(n) - single pass through items
        Space complexity: O(1) - constant space for counter and mapping
        """
        types = {"type": 0, "color": 1, "name": 2}
        matching_items = 0

        for item in items:
            matching_items += item[types[ruleKey]] == ruleValue

        return matching_items
