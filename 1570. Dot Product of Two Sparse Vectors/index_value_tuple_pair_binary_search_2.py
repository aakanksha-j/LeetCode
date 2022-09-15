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

"""https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/1749065/Binary-search-O(min(m-n)-*-log(max(m-n))
I got this question today on my FB interview. I proposed the Hash solution, and he asked the downside to it. I responded with large size of sparse vectors, hash collisions will occur when we hit memory allocation limits, etc. He asked alternative solutions and I proposed array of (index, value) pair. He asked me to code that. Then he added a constraint where one vector is considerably smaller than the other, and asked if we can improve the time complexity from O(m+n). After some scratching around, I told them that we can by doing binary-search of small vector's index over the larger one. This should improve the time-complexity. Was not sure of the exact Big Oh, but it should be better than m * log(n), since the search space should keep reducing from n. Fingers crossed for the results

smaller or larger does not make them less or more sparse. For example, a vector could have 1 billion numbers, out of which only 10 million are non zeroes. This would be a very large list and still sparse vector. In a hash table, a common issue is hash collision. Typically we reduce collision by over allocating. For example, for a 10 million entry hash table, we might allocate memory for say 13 million entries based on 0.75% load factor. When we hash such large lists (I know 10 million ints is not really that large, but there are other items in memory and imagine many such parallel calculations being done) , we may start hitting memory limits so over allocating gets difficult, and we get too many hash collisions. Smaller in the context meant (and the interviewer gave me some similar numbers), 1 vector was 1 billion numbers and the other vector had only 1 million or less entries
"""
