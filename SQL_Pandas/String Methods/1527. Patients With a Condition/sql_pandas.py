"""
https://leetcode.com/problems/patients-with-a-condition/

1527. Patients With a Condition
Easy
SQL Schema
Table: Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
 

Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
Output: 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+
Explanation: Bob and George both have a condition that starts with DIAB1.
"""

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.startswith('DIAB1') | patients['conditions'].str.contains(' DIAB1')]

# Write your MySQL query statement below
# SELECT *
# FROM Patients
# WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'


"""SUBSTRING(column_name, start, length): This extracts a substring from a column's values, starting at the specified start position, and up to the specified length.

UPPER(expression): This converts a string expression to uppercase.

LOWER(expression): This converts a string expression to lowercase.

CONCAT(string1, string2, ...): This concatenates two or more strings into one."""