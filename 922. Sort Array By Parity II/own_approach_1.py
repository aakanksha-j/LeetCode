class Solution:
    """Approach 1: Own approach using even and odd pointer.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 208 ms
       Memory: 16.3 MB"""
    def sortArrayByParityII(self, A):
        i, j = 0, 1
        while i <= len(A)-2 and j <= len(A)-1:
            if A[i]%2 > A[j]%2: # swap when different from expected
                A[i], A[j] = A[j], A[i]
            if A[i]%2 == 0: # increase when expected
                i += 2
            if A[j]%2 == 1: # increase when expected
                j += 2
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
