"""
1491. Average Salary Excluding the Minimum and Maximum Salary
Easy
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
 

Constraints:

3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
"""

import math


class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = math.inf
        max_sal = -math.inf
        sum = 0
        for sal in salary:
            sum += sal
            if sal < min_sal:
                min_sal = sal
            if sal > max_sal:
                max_sal = sal
        return (sum - min_sal - max_sal) / (len(salary) - 2)
        
        # min_sal = math.inf
        # max_sal = -math.inf
        # sum = 0
        # for s in salary:
        #     sum += s
        #     min_sal = min(min_sal, s)
        #     max_sal = max(max_sal, s)

        # return (sum - min_sal - max_sal) / (len(salary) - 2)
        #return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)