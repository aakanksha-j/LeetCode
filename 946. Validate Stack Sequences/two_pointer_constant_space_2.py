# https://leetcode.com/problems/validate-stack-sequences/discuss/3410723/Image-Explanation-2-Approaches%3A-2-Pointer-O(1)-and-Stack-O(N)-C%2B%2BJavaPython
# https://www.youtube.com/watch?v=lqP82OhRkAA&ab_channel=AryanMittal

# input array pushed is modified

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, 0
        for value in pushed:
            print(pushed, popped, i, j)
            pushed[i] = value
            print(pushed)
            i += 1
            while i > 0 and pushed[i - 1] == popped[j]:
                print(i, j, pushed[i-1], popped[j])
                i -= 1
                j += 1
        return i == 0 # i-1 will check for pushed[0]
    

# O(n) time
# O(1) space

# testcase 1: pushed = [1,2,3,4,5], popped = [4,5,3,2,1] output = true
# testcase 2: pushed = [1,2,3,4,5], popped = [4,3,5,1,2] output = false

# output: 
"""
[1, 2, 3, 4, 5] [4, 5, 3, 2, 1] 0 0
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [4, 5, 3, 2, 1] 1 0
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [4, 5, 3, 2, 1] 2 0
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [4, 5, 3, 2, 1] 3 0
[1, 2, 3, 4, 5]
4 0 4 4
[1, 2, 3, 4, 5] [4, 5, 3, 2, 1] 3 1
[1, 2, 3, 5, 5] # modified input
4 1 5 5
3 2 3 3
2 3 2 2
1 4 1 1
[1, 2, 3, 4, 5] [4, 3, 5, 1, 2] 0 0
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [4, 3, 5, 1, 2] 1 0
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [4, 3, 5, 1, 2] 2 0
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5] [4, 3, 5, 1, 2] 3 0
[1, 2, 3, 4, 5]
4 0 4 4
3 1 3 3
[1, 2, 3, 4, 5] [4, 3, 5, 1, 2] 2 2
[1, 2, 5, 4, 5]  # modified input
3 2 5 5
i j 
after while loop, i, j = 2, 3
pushed[i-1] = pushed[1] = 2
popped[j] = popped[3] = 1
1 cannot be popped before 2 so while loop does not execute and since for loop ends after 5 iterations, i != 0, return False
"""