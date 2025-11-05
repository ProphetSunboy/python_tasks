class Helper:
    def __init__(self, x):
        self.x = x
        self.result = 0
        self.large = SortedList()
        self.small = SortedList()
        self.occ = defaultdict(int)

    def insert(self, num):
        if self.occ[num] > 0:
            self.internal_remove((self.occ[num], num))
        self.occ[num] += 1
        self.internal_insert((self.occ[num], num))

    def remove(self, num):
        self.internal_remove((self.occ[num], num))
        self.occ[num] -= 1
        if self.occ[num] > 0:
            self.internal_insert((self.occ[num], num))

    def get(self):
        return self.result

    def internal_insert(self, p):
        if len(self.large) < self.x or p > self.large[0]:
            self.result += p[0] * p[1]
            self.large.add(p)
            if len(self.large) > self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0] * to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(p)

    def internal_remove(self, p):
        if p >= self.large[0]:
            self.result -= p[0] * p[1]
            self.large.remove(p)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0] * to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(p)


class Solution:
    def findXSum(self, nums, k, x):
        """
        Returns the x-sum for each k-length sublist in nums.

        The x-sum of a list is computed as follows:
            1. Count the frequency of each element in the list.
            2. Find the top x most frequent elements. If there are ties in frequency,
            the element with the larger value is preferred.
            3. Reconstruct a list using only occurrences of those top x elements.
            4. The x-sum is the sum of this resulting array.
            5. If there are fewer than x distinct elements, the x-sum is the sum of the list.

        Args:
            nums (List[int]): The input list of integers.
            k (int): Length of each sublist window to consider.
            x (int): Number of top frequent elements to include in the x-sum.

        Returns:
            List[int]: A list where each entry is the x-sum of nums[i:i+k].

        Example:
            nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
            Output: [6, 10, 12]

        Time Complexity: O(n log x), where n is the length of nums.
        Space Complexity: O(n)
        """
        helper = Helper(x)
        ans = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                ans.append(helper.get())

        return ans
