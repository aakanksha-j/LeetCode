class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeroes = [(i, val) for i, val in enumerate(nums) if val]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        def binary_search(left, right, arr, target):
            while left <= right:
                mid = left + (right - left) // 2
                if target == arr[mid][0]:
                    return mid
                elif target < arr[mid][0]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        a, b = self.non_zeroes, vec.non_zeroes
        if len(a) > len(b):
            a, b = b, a

        j, total = 0, 0
        for i, val in a:
            idx = binary_search(j, len(b) - 1, b, i)
            if idx != -1:
                total += val * b[idx][1]
                j += 1

        return total



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
