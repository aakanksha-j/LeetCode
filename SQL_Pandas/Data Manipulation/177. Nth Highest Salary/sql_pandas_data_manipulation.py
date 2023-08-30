"""177. Nth Highest Salary
Medium
SQL Schema
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
"""

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates('salary')
    if len(df['salary'].unique()) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    df = df.sort_values('salary', ascending = False)
    df.drop('id', axis = 1, inplace = True)
    return df.head(N).tail(1)

# https://leetcode.com/problems/nth-highest-salary/discuss/53041/Accpted-Solution-for-the-Nth-Highest-Salary
# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
# DECLARE M INT;
# SET M = N - 1;
#   RETURN (
#       # Write your MySQL query statement below.
#       SELECT 
#         IFNULL(
#             NULL, 
#             (SELECT DISTINCT salary 
#             FROM Employee
#             ORDER BY salary DESC
#             LIMIT 1 OFFSET M
#         )
#   )
# );
# END