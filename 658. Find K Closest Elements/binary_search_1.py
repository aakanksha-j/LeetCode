class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
        
        # testcase A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3
        
        # time O(N - k) to binary search and find result
        # space O(k) to return list of size k
        
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left: left + k]
        
        