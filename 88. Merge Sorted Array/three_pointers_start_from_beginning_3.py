class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Three pointers, start from the beginning
        # time O(n + m)
        # space O(m)
        
        i, j, k = 0, 0, 0
        nums1_copy = nums1[:m]
        for k in range(m + n): 
            if (j >= n) or (i < m and nums1_copy[i] <= nums2[j]): 
                # list index out of range error if j part is written later as i may go beyond m
                nums1[k] = nums1_copy[i]
                i += 1    
            else:
                nums1[k] = nums2[j]
                j += 1
                
        return nums1