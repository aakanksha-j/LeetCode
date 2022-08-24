class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # leetcode solution - presum + hashmap
        # sum[i] - sum[j] = 0 then sum of elements between indices i and j is 0, similaryly sum[i] - sum[j] = k then
        # sum of elements between these two indices is k, therefore just compare sum[j] - k with sum[i]
        # eg. [7,3,4,-4,-3,0,5,2], k= 7

        # time: O(N) - iterate over every element
        # space: O(N) - for hashmap

        # cannot use two pointers, for sliding window, will have to find min element and then run

        nums_dic = {0: 1}
        count, pre_sum = 0, 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if (pre_sum - k) in nums_dic:
                count += nums_dic[pre_sum - k]
            nums_dic[pre_sum] = nums_dic.get(pre_sum, 0) + 1

        return count

        
