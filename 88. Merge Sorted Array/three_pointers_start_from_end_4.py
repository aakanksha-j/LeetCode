class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Three pointers, start from the end
        # time O(n + m)
        # space O(1) constant space, most efficient
        
        i, j = m - 1, n - 1
        nums1_copy = nums1[:m]
        for k in range(m + n - 1, -1, -1): 
            if j < 0:
                break
            if (i > -1) and (nums1[i] > nums2[j]): 
                nums1[k] = nums1[i]
                i -= 1    
            else:
                nums1[k] = nums2[j]
                j -= 1
                
        return nums1
            