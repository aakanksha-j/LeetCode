class Solution:
    """Approach 1:
       Time complexity: O(n)
       Space complexity: O(n)
       Runtime: 116 ms
       Memory: 17.5 MB
    """
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # using bucket sort and sliding window. window of size t + 1.
        dict = {}
        window = t + 1
        for i, value in enumerate(nums):
            key = value // window

            if key in dict: # both elements are in same bucket
                return True

            # both elements are in neighbour buckets
            if key - 1 in dict and abs(value - dict[key - 1]) < window:
                return True
            if key + 1 in dict and abs(value - dict[key + 1]) < window:
                return True

            dict[key] = value

            if i >= k: # Remove the bucket which is too far away
                del dict[nums[i - k] // window]

        return False


def main():
    numbers = [1,2,3,1]
    k = 3
    t = 0
    s=Solution()
    print(s.numFriendRequests(numbers, k, t))
    numbers = [1,0,1,1]
    k = 1
    t = 2
    print(s.numFriendRequests(numbers, k, t))
    numbers = [1,5,9,1,5,9]
    k = 2
    t = 3
    print(s.numFriendRequests(numbers, k, t))

if __name__ == '__main__':
    main()

"""https://leetcode.com/problems/contains-duplicate-iii/discuss/61639/JavaPython-one-pass-solution-O(n)-time-O(n)-space-using-buckets
https://leetcode.com/problems/contains-duplicate-iii/discuss/824578/C%2B%2B-O(N)-time-complexity-or-Explained-or-Buckets-or-O(K)-space-complexity"""
