"""
258. Add Digits
Easy
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

# O(1) time and space

# own approach
class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        output = num % 9
        if output == 0:
            return 9
        
        return output 
    
# one liner
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num-1) % 9 if num else 0
    
"""
digital root in decimal system
dr = 0, if n = 0
dr = 9, if n = 9k
dr = n mod 9, if n != 9k 

last two reduced to
dr = 0, if n = 0
dr = 1 + (n-1) mod 9, if n != 0
"""