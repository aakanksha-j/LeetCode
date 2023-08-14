"""
279. Perfect Squares
Medium
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
"""
class Solution:
    def numSquares(self, n: int) -> int:
        # using queue bfs - leetcode solution approach 4
        
        # time O(n^(h/2)) where h is height of n-ary tree, the recursive calls form a complete N-ary tree, worst case - we have to traverse entire tree to find the solution, maximum height of tree will be 4, so runtime is O(square root of n)
        # space O(square root of n) since we keep a list of squares and recursive calls using queue
        
        # eg. n = 88, 36 + 36 + 16, level 3
        # n = 1, level 1
        
        squares_list = [i**2 for i in range(1, int(n**.5) + 1)] # only upto 1 + square root of n
        queue = {n} # queue is a set, not list
        level = 0
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square in squares_list:
                    if remainder < square:
                        break
                    elif remainder == square:
                        return level
                    else:
                        next_queue.add(remainder - square)
            queue = next_queue
        return level

# wrong answer for 88, level 4 instead of 3     
        
#         squares = {1}
        
#         i = 2
#         while i**2 <= n:
#             squares.add(i**2)
#             i += 1
        
#         squares_list = sorted(squares)
#         print(squares_list)
#         len_list = len(squares_list)
        
#         min_count = n
#         for i in range(len_list - 1, -1, -1):
#             # multiple of n
#             print(i, squares_list[i])
#             if n % squares_list[i] == 0: 
#                 min_count = min(n // squares_list[i], min_count)
#                 continue
                
#             remainder = n - squares_list[i]
#             print(remainder)
#             count_square_numbers = 1
            
#             while remainder > 0:
#                 print(remainder)
#                 if remainder in squares:
#                     remainder -= remainder
#                 else:
#                     remainder -= int(sqrt(remainder))**2
#                 count_square_numbers += 1
            
#             if remainder == 0:
#                 min_count = min(count_square_numbers, min_count)
            
#             if min_count < 3: return min_count

#         return min_count
                        
                    
                
        
            