class Solution:
    """Approach 3: Use a flag for uphill traversal.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 220 ms
       Memory: 15.1 MB"""
    def validMountainArray(self, A):
        n=len(A)
        if n<3 or A[0] >= A[1]:
            return False
        flag = True # uphill flag
        for i in range(1,n-1):
            if flag: # going uphill
                if A[i] >= A[i+1]:
                    flag = False
            if not flag: # going downhill
                if A[i] <= A[i+1]:
                    return False
        return not flag
def main():
    numbers =[0,1,0]
    s=Solution()
    print(s.validMountainArray(numbers))
    numbers =[0,3,2,1]
    print(s.validMountainArray(numbers))
    numbers =[0,0,0]
    print(s.validMountainArray(numbers))
    numbers =[0,1,1]
    print(s.validMountainArray(numbers))
    numbers =[1,0,0]
    print(s.validMountainArray(numbers))
    numbers =[0,0,1]
    print(s.validMountainArray(numbers))
    numbers =[-1,0,1]
    print(s.validMountainArray(numbers))
    numbers =[1,0,-1]
    print(s.validMountainArray(numbers))
    numbers =[1,1,0]
    print(s.validMountainArray(numbers))
    numbers =[1,0,1]
    print(s.validMountainArray(numbers))
    numbers =[0,1,2,3,4,5,6,7,8,9]
    print(s.validMountainArray(numbers))
    numbers =[]
    print(s.validMountainArray(numbers))

if __name__ == '__main__':
    main()

# Expected output: First two true, rest false.
