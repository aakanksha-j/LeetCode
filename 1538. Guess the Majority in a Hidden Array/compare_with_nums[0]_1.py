"""1538. Guess the Majority in a Hidden Array
Medium
We have an integer array nums, where all the integers in nums are 0 or 1. You will not be given direct access to the array, instead, you will have an API ArrayReader which have the following functions:

int query(int a, int b, int c, int d): where 0 <= a < b < c < d < ArrayReader.length(). The function returns the distribution of the value of the 4 elements and returns:
4 : if the values of the 4 elements are the same (0 or 1).
2 : if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
0 : if two element have a value equal to 0 and two elements have a value equal to 1.
int length(): Returns the size of the array.
You are allowed to call query() 2 * n times at most where n is equal to ArrayReader.length().

Return any index of the most frequent value in nums, in case of tie, return -1.

 

Example 1:

Input: nums = [0,0,1,0,1,1,1,1]
Output: 5
Explanation: The following calls to the API
reader.length() // returns 8 because there are 8 elements in the hidden array.
reader.query(0,1,2,3) // returns 2 this is a query that compares the elements nums[0], nums[1], nums[2], nums[3]
// Three elements have a value equal to 0 and one element has value equal to 1 or viceversa.
reader.query(4,5,6,7) // returns 4 because nums[4], nums[5], nums[6], nums[7] have the same value.
we can infer that the most frequent value is found in the last 4 elements.
Index 2, 4, 6, 7 is also a correct answer.
Example 2:

Input: nums = [0,0,1,1,0]
Output: 0
Example 3:

Input: nums = [1,0,1,0,1,0,1,0]
Output: -1
 

Constraints:

5 <= nums.length <= 105
0 <= nums[i] <= 1
 

Follow up: What is the minimum number of calls needed to find the majority element?"""

# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        # leetcode solution - https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/solution/
        # time O(n), space O(1)
        # compare every value with value at index 0 and decide accordingly
        # we will do n calls, 4 calls for 0123 and from 4 to n (n-4) calls
        
        n = reader.length()
        cnt_equal = 1 # compare with nums[0]
        cnt_differ = 0
        diff_index = -1
        
        def f(r0, curr, i):
            nonlocal cnt_equal, cnt_differ, diff_index
            # print(r0, curr, i)
            if r0 == curr:
                cnt_equal += 1
                # print(cnt_equal, 'c')
            else:
                cnt_differ += 1
                diff_index = i
                # print(diff_index)

        # to find nums[1]
        r0234, r1234 = reader.query(0,2,3,4), reader.query(1,2,3,4)
        f(r0234, r1234, 1)
        
        # to find nums[2]
        r0134 = reader.query(0,1,3,4)
        f(r0134, r1234, 2)
        
        # to find nums[3]
        r0124 = reader.query(0,1,2,4)
        f(r0124, r1234, 3)
        
        r0123 = reader.query(0,1,2,3)
        for i in range(4, n):
            r123i = reader.query(1,2,3,i)
            f(r0123, r123i, i)
                
        # print(cnt_equal, cnt_differ, diff_index)
        return -1 if cnt_equal == cnt_differ else 0 if cnt_equal > cnt_differ else diff_index
        # if cnt_equal == cnt_differ:
        #     return -1
        # elif cnt_equal > cnt_differ:
        #     return 0
        # else:
        #     return diff_index
        