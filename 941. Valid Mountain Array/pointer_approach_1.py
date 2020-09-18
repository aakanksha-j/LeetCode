class Solution:
    """Approach 1: Traverse array with one pointer and determine peak pointer
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 256 ms
       Memory: 15.1 MB"""
    def validMountainArray(self, A):
        if len(A)<3: return False
        pointer=1
        while pointer<len(A) and A[pointer]>A[pointer-1]:
            pointer+=1
        p_pointer=pointer-1
        flag=False
        while pointer<len(A) and A[pointer]<A[pointer-1]:
            flag=True
            pointer+=1
        if pointer==len(A) and p_pointer>0 and flag:
            return True
        return False

def main():
    numbers = [0,3,2,1]
    #[0,0,0], [0,1,0], [0,1,1],[1,1,0],[0,0,1],[-1,0,1],[1,0,-1],[1,1,0],[1,0,1]
    # failed at [0,1,2,3,4,5,6,7,8,9]
    s=Solution()
    print(s.validMountainArray(numbers))

if __name__ == '__main__':
    main()
