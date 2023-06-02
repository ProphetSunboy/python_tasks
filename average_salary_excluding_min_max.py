class Solution:
    def average(self, salary: List[int]) -> float:
        """
        Given an array of unique integers salary where salary[i] is the salary
        of the ith employee.
        Return the average salary of employees excluding the minimum and
        maximum salary. 
        """
        max_s = salary[0]
        min_s = salary[0]
        length = 0
        s_sum = 0
        for s in salary:
            if s > max_s:
                max_s = s
            if s < min_s:
                min_s = s
            s_sum += s
            length += 1
        return (s_sum - max_s - min_s) / (length - 2)