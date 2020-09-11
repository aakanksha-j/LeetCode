class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=m-1,n-1,m+n-1
        while i>-1 and j>-1:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while i>-1:
            nums1[k]=nums1[i]
            k-=1
            i-=1
        while j>-1:
            nums1[k]=nums2[j]
            k-=1
            j-=1

def main():
    nums1 = [1,7,7]
    m = 3
    nums2 = []
    n = 0
    s=Solution()
    s.merge(nums1,m,nums2,n)
    print(nums1)

if __name__ == '__main__':
    main()
