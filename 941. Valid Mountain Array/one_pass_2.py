class Solution:
    """Approach 2: Walk uphill from left to right, until we can't - that has to be the
       peak. We will have to ensure it is not first and last element. Again walk
       downhil. If we reach end of array, mountain is valid, otherwise not.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 224 ms
       Memory: 15 MB"""
    def validMountainArray(self, A):
        n=len(A)
        if len(A)<3 or A[0]>=A[1]: return False
        pointer=1
        while pointer+1<len(A) and A[pointer]<A[pointer+1]:
            pointer+=1
        if pointer==0 or pointer==n-1:
            return False
        while pointer+1<len(A) and A[pointer]>A[pointer+1]:
            pointer+=1
        return pointer==n-1

def main():
    numbers =[0,3,2,1]
    # [0,0,0], [0,1,0], [0,1,1],[1,1,0],[0,0,1],[-1,0,1],[1,0,-1],[1,1,0],[1,0,1]
    # [0,1,2,3,4,5,6,7,8,9], []
    s=Solution()
    print(s.validMountainArray(numbers))

if __name__ == '__main__':
    main()
