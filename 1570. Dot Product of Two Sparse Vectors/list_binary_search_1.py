class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1 = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0

        # make smaller array vector 1, and bigger array vector 2
        print(self.v1, vec.v1)
        if len(self.v1) <= len(vec.v1):
            vec1, vec2 = self.v1, vec.v1
            m, n = len(vec1), len(vec2)
        else:
            vec1, vec2 = vec.v1, self.v1
            m, n = len(vec1), len(vec2)

        # run binary search on bigger array, search for value of smaller array elements
        for i in range(m):
            if vec1[i] == 0:
                continue
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if i == mid:
                    output += vec1[i]*vec2[mid]
                    break
                elif i < mid:
                    right = mid - 1
                else:
                    left = mid + 1
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
