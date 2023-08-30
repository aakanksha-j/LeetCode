"""
176. Second Highest Salary
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
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

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
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

# Write your MySQL query statement below
# SELECT 
#     IFNULL 
#     ((SELECT DISTINCT Salary
#         FROM Employee
#         ORDER BY Salary DESC
#         LIMIT 1 OFFSET 1), # limit will return 1 record and offset will return after highest
#     NULL)
#     as SecondHighestSalary

import numpy as np
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])
    if len(employee['salary']) < 2:
        return pd.DataFrame({'SecondHighestSalary': [np.NaN]})
    employee = employee.sort_values(by = 'salary', ascending = False)
    employee.drop('id', axis = 1, inplace = True)
    employee.rename({'salary':'SecondHighestSalary'}, axis = 1, inplace = True)
    return employee.head(2).tail(1)

# steps:
# 1. Drop any duplicate salaries
# 2. If there are less than two unique salaries, return 'np.NaN'.
# 3. Sort the table by 'salary' in descending order
# 4. Drop the 'id' column
# 5. Rename the 'salary' column
# 6. Return the second highest salary