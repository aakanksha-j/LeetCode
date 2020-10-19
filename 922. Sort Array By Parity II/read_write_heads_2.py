"""https://leetcode.com/problems/sort-array-by-parity-ii/solution/"""
class Solution:
    """Approach 1: When element at position is not as expected, swapping takes
                   place. For loop to increase even (i) positions, while loop
                   to increase odd (j) positions.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 196 ms
       Memory: 16.3 MB"""
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0,len(A),2):
            if A[i]%2: # if A[i] is odd, modulo results in 1.
                while A[j]%2: # while A[j] is odd as expected, increase position
                    j += 2
                A[i], A[j] = A[j], A[i] 
        return A

def main():
    numbers =[3,1,2,4,5,6]
    s=Solution()
    print(s.sortArrayByParityII(numbers))
    numbers = [0,0,1,1]
    print(s.sortArrayByParityII(numbers))
    numbers = [0,1,0,1]
    print(s.sortArrayByParityII(numbers))
    numbers = [1,0,1,0]
    print(s.sortArrayByParityII(numbers))
    numbers = [1,1,0,0]
    print(s.sortArrayByParityII(numbers))

if __name__ == '__main__':
    main()
